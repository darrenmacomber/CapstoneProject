from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BookItem

def index(request):
    return render(request, 'APILibraryApp/index.html')
