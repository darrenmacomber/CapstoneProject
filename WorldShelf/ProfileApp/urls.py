from django.urls import path
from . import views

app_name = 'ProfileApp'
urlpatterns = [
    path('', views.index, name='profile'),
]
