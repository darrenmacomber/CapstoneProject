from django.urls import path
from . import views

app_name = 'ProfileApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('getUsers/', views.getUsers, name='getUsers'),
    path('getTags/', views.getTags, name='getTags'),
    path('edit/', views.editProfile, name='editProfile'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),
    path('userProfile/<str:username>/', views.userProfile, name='userProfile'),
    path('saveBook/', views.saveBook, name='saveBook'),
    path('saveTags/', views.saveTags, name='saveTags'),
    path('searchProfiles/', views.searchProfiles, name='searchProfiles'),
]
