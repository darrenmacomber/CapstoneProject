from django.urls import path
from . import views

app_name = 'APILibraryApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('bookSearch/', views.bookSearch, name='bookSearch'),
    path('saveBook/', views.saveBook, name='saveBook'),
    path('tagSearch/', views.tagSearch, name='tagSearch'),
    path('getTags/', views.getTags, name='getTags'),
    path('getUserBooks/', views.getUserBooks, name='getUserBooks'),
    path('saveTags/', views.saveTags, name='saveTags'),
    path('bookTags/', views.bookTags, name='bookTags'),
    path('findTaggedBooks/', views.findTaggedBooks, name='findTaggedBooks'),
]
