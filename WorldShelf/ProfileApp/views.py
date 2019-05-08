from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.apps import apps

apps.get_model('APILibraryApp', 'Book', require_ready=True)
apps.get_model('APILibraryApp', 'Author', require_ready=True)
apps.get_model('APILibraryApp', 'Category', require_ready=True)
apps.get_model('APILibraryApp', 'UserTag', require_ready=True)
#from .models import Book, Author, Category, UserTag
#from ..APILibraryApp.models import Book, Author, Category, UserTag

import json

def index(request):
    return render(request, 'ProfileApp/index.html')
