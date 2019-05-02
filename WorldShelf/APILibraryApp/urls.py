from django.urls import path
from . import views

app_name = 'APILibraryApp'
urlpatterns = [
    path('index/', views.index, name='index')
]
