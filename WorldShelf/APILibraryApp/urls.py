from django.urls import path
from . import views

app_name = 'APILibraryApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('saveBook', views.saveBook, name='saveBook'),
]
