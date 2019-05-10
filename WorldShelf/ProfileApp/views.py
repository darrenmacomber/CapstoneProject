from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.apps import apps
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .secrets import google_books_api_key
from APILibraryApp.models import Book, Author, Category, UserTag
from APILibraryApp.views import saveBook

import json, datetime

def updateProfile(request):
    data = json.loads(request.body)
    print(data)
    username = request.user
    target_profile = UserProfile.objects.get(username=data['username'])
    target_profile.first_name = data['first_name']
    target_profile.last_name = data['last_name']
    target_profile.birthday = datetime.datetime.strptime(data['birthday'], '%Y-%m-%d')
    target_profile.location = data['location']
    target_profile.description = data['description']
    target_profile.save()
    return HttpResponse('success')

def profile(request, username):
    target_profile = UserProfile.objects.get(username=username)
    context = {
        'profile': target_profile,
        'username': target_profile.username,
        'first_name': target_profile.first_name,
        'last_name': target_profile.last_name,
        'birthday': target_profile.birthday,
        'location': target_profile.location,
        'description': target_profile.description,
        'key': google_books_api_key
    }
    print(target_profile)
    return render(request, 'ProfileApp/profile.html', context)

@login_required
def editprofile(request):
    return render(request, 'ProfileApp/editprofile.html')
