from django.contrib import admin

from .models import Book, Author, Category, UserTag, UserBook

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(UserTag)
admin.site.register(UserBook)
