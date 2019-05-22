from django.shortcuts import render, reverse
from django.apps import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ProfileApp.models import UserProfile

'''Renders Register/Login Page'''
def register_login(request):
    return render(request, 'users/register_login.html')

'''Registers User and also creates a UserProfile instance'''
# Standard User registration function.
# Creates a UserProfile instance using info entered from the request.
def register_user(request):
    username = request.POST['username']
    if User.objects.filter(username = username).exists():
        return HttpResponseRedirect(reverse('users:protected'))
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    birthday = request.POST['birthday']
    location = request.POST['location']
    description = request.POST['description']
    user = User.objects.create_user(username, email, password)
    userprofile = UserProfile(user=user, username=username, first_name=first_name, last_name=last_name, birthday=birthday, location=location, description=description, spoiler_protection=False)
    userprofile.save()
    login(request, user)
    return HttpResponseRedirect(reverse('users:protected'))

'''Login functions'''
@login_required
def protected(request):
    print(request.user.username) # able to access the user immediately
    return render(request, 'users/protected.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('users:protected'))
    return HttpResponseRedirect(reverse('users:register_login'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:register_login'))
