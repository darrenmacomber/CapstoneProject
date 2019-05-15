from django.urls import path
from . import views

app_name = 'APILibraryApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('bookSearch/', views.bookSearch, name='bookSearch'),
    path('saveBook/', views.saveBook, name='saveBook'),
    path('tagSearch/', views.tagSearch, name='tagSearch'),
    path('getTags/', views.getTags, name='getTags'),
    path('saveTags/', views.saveTags, name='saveTags'),
]
