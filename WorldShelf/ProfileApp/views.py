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

def searchProfiles(request):
    return render(request, 'ProfileApp/searchProfiles.html')

def spoilerProtection(request):
    current_user = request.user
    target_profile = UserProfile.objects.get(username=current_user)
    data = {'spoiler_protection': []}
    data['spoiler_protection'].append({
        'spoiler_protection': target_profile.spoiler_protection,
        })
    return JsonResponse(data)

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

@login_required
def editProfile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('users/register_login.html')
    return render(request, 'ProfileApp/editProfile.html')
