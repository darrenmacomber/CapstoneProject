from django.urls import path
from . import views

app_name = 'ProfileApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('searchProfiles/', views.searchProfiles, name='searchProfiles'),
    path('spoilerProtection/', views.spoilerProtection, name='spoilerProtection'),
    path('getUsers/', views.getUsers, name='getUsers'),
    path('updateProgress/', views.updateProgress, name='updateProgress'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),
    path('userProfile/<str:username>/', views.userProfile, name='userProfile'),
    path('getComments/', views.getComments, name = 'getComments'),
    path('makeComment/', views.makeComment, name='makeComment'),
    path('removeBook/', views.removeBook, name='removeBook'),
    path('editProfile/<str:username>/', views.editProfile, name='editProfile'),
]
