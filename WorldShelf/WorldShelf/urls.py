from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APILibraryApp/', include('APILibraryApp.urls')),
    path('users/', include('users.urls')),
]
