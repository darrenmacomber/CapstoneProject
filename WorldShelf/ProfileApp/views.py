from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.apps import apps
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .secrets import google_books_api_key
from APILibraryApp.models import Book, Author, Category, UserTag, UserBook, UserComment

import json, datetime


def index(request):
    return HttpResponse('ok')

'''Renders Profile search page'''
def searchProfiles(request):
    return render(request, 'ProfileApp/searchProfiles.html')

'''Checks UserProfile instance to see if spoiler protection is enabled'''
# Input includes current user.
# Checks the UserProfile associated with the current user's username
# Retrives boolean info from the UserProfile's spoiler_portection parameter and sends to vue in json.
def spoilerProtection(request):
    current_user = request.user
    target_profile = UserProfile.objects.get(username=current_user)
    data = {'spoiler_protection': []}
    data['spoiler_protection'].append({
        'spoiler_protection': target_profile.spoiler_protection,
        })
    return JsonResponse(data)

'''Retrieves a list of all Users and their parameters'''
# Checks database for User model instances
# Parses info from each user's associated profile into json data to send to vue.
def getUsers(request):
    data = {'users': []}
    user_array = User.objects.all()
    for user in user_array:
        username = user.username
        profile = user.profile
        data['users'].append({
            'username': username,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'birthday': profile.birthday,
            'prettybirthday': profile.prettybirthday(),
            'location': profile.location,
            'description': profile.description,
        })
    return JsonResponse(data)

'''Upadates the page the user is currently on in their specific book'''
# Checks for login.
# Checks for correct User instance associated with this UserProfile.
# Retrieves updated progress point page from the json input.
# Finds UserBook instance associated with user, if it exists, and updates its progress_point parameter.
# Returns HTTP response confirmation.
def updateProgress(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        user = request.user
        bookID = data['bookID']
        progress_point = data['progress_point']
        if Book.objects.filter(bookID=bookID).exists():
            target_book = Book.objects.get(bookID=bookID)
        print(target_book.userbooks)
        if target_book.userbooks.filter(user=user).exists():
            target_userbook = target_book.userbooks.get(user=user)
            target_userbook.progress = progress_point
            target_userbook.save()
            return HttpResponse('success')
    return HttpResponse('failure')

'''Updates the info in a specific user's profile page'''
# Doesn't check for login as this is only rendered on the @protected page.
# Retrieves new profile parameters from json input.
# Finds UserProfile instance associated with current username.
# Updates parameters and sends HTTP response confirmation.
def updateProfile(request):
    data = json.loads(request.body)
    username = request.user
    target_profile = UserProfile.objects.get(username=data['username'])
    target_profile.first_name = data['first_name']
    target_profile.last_name = data['last_name']
    target_profile.birthday = datetime.datetime.strptime(data['birthday'], '%Y-%m-%d')
    target_profile.location = data['location']
    target_profile.description = data['description']
    target_profile.spoiler_protection = data['spoiler_protection']
    target_profile.save()
    return HttpResponse('success')

'''Creates an instance of the UserProfile model'''
# Called automatically during the User creation function.
# Params set by input fields on register_login page.
# Associates new UserProfile instance with User's username.
def userProfile(request, username):
    target_profile = UserProfile.objects.get(username=username)
    context = {
        'profile': target_profile,
        'username': target_profile.username,
        'first_name': target_profile.first_name,
        'last_name': target_profile.last_name,
        'birthday': target_profile.birthday,
        'prettybirthday': target_profile.prettybirthday(),
        'location': target_profile.location,
        'description': target_profile.description,
        'spoiler_protection': target_profile.spoiler_protection,
        'key': google_books_api_key,
        'profile_user': target_profile.user
    }
    return render(request, 'ProfileApp/userProfile.html', context)

'''Retrieves all Comments associated with this specific Book'''
# bookID retrieved from json input.
# Searches Book instances for Book with that bookID.
# searchs that book .comments for all objects and sends to vue as json response.
def getComments(request):
    bookID = request.GET['bookID']
    data = {'comments': []}
    if Book.objects.filter(bookID = bookID).exists():
        target_book = Book.objects.get(bookID = bookID)
        for comment in target_book.comments.all():
            data['comments'].append({
                'book': comment.book.title,
                'user': comment.user.username,
                'text': comment.text,
                'progress_point': comment.progress_point,
                'date_created': comment.prettycreatedate(),
                'date_edited': comment.prettyeditdate(),
            })
    return JsonResponse(data)

'''Adds Comment to be associated with this Book'''
# Checks for login.
# bookID retrieved from json input.
# After searching Book instances for the Book with that bookID, creates Comment associated with Book.
def makeComment(request):
    if not request.user.is_authenticated:
        return HttpResponse('failure')
    data = json.loads(request.body)
    bookID = data['bookID']
    target_book = Book.objects.get(bookID = bookID)
    user = request.user
    progress_point = data['progress_point']
    text = data['text']
    usercomment = UserComment(book=target_book, user=user, progress_point = progress_point, text = text)
    usercomment.save()
    return HttpResponse('success')

'''Removes Book from UserProfile'''
# This function actually removes the UserBook instance rather than the Book.
# Checks for login.
# Checks for correct User instance associated with this UserProfile.
# bookID finds the target Book instance.
# username from json response used to find the UserBook associated with that Book.
# UserBook is deleted and HTTP confirmation is returned.
def removeBook(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        bookID = data['bookID']
        target_book = Book.objects.get(bookID = bookID)
        if target_book.userbooks.filter(user=request.user).exists():
            target_userbook = target_book.userbooks.get(user=request.user)
            target_userbook.delete()
            return HttpResponse('success')
        return HttpResponse('failure2')
    return HttpResponse('failure1')

'''Renders the Edit Profile page'''
@login_required
def editProfile(request):
    context = {
        'username': user.username,
    }
    if not request.user.is_authenticated:
        return HttpResponseRedirect('users/register_login.html')
    return render(request, 'ProfileApp/editProfile.html', context)
