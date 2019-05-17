from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.apps import apps
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .secrets import google_books_api_key
from APILibraryApp.models import Book, Author, Category, UserTag, UserBook
from APILibraryApp.views import saveBook, getTags, saveTags, getUserBooks

import json, datetime

def index(request):
    return HttpResponse('ok')

def searchProfiles(request):
    return render(request, 'ProfileApp/searchProfiles.html')

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

def updateProfile(request):
    data = json.loads(request.body)
    username = request.user
    target_profile = UserProfile.objects.get(username=data['username'])
    target_profile.first_name = data['first_name']
    target_profile.last_name = data['last_name']
    target_profile.birthday = datetime.datetime.strptime(data['birthday'], '%Y-%m-%d')
    target_profile.location = data['location']
    target_profile.description = data['description']
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
        'key': google_books_api_key,
        'profile_user': target_profile.user
    }
    return render(request, 'ProfileApp/userProfile.html', context)

@login_required
def editProfile(request):
    return render(request, 'ProfileApp/editProfile.html')
