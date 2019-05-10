from django.urls import path
from . import views

app_name = 'ProfileApp'
urlpatterns = [
    path('', views.editprofile, name='editprofile'),
    path('updateProfile/', views.updateProfile, name='updateProfile'),
    path('<str:username>/', views.profile, name='profile')
]
