from django.urls import path
from . import views

app_name = 'ProfileApp'
urlpatterns = [
    path('getUsers/', views.getUsers, name='getUsers'),
    path('edit/', views.editProfile, name='editProfile'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),
    path('userProfile/<str:username>/', views.userProfile, name='userProfile'),
    path('saveBook/', views.saveBook, name='saveBook'),
    path('searchProfiles/', views.searchProfiles, name='searchProfiles'),
]
