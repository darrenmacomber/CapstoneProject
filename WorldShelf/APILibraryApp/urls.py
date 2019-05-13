from django.urls import path
from . import views

app_name = 'APILibraryApp'
urlpatterns = [
    path('bookSearch', views.bookSearch, name='bookSearch'),
    path('saveBook', views.saveBook, name='saveBook'),
]
