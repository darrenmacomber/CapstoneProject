from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    bookID = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')
    languages = models.CharField(max_length=200)
    page_count = models.IntegerField()
    publish_date = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    isbn = models.TextField()
    ebook = models.BooleanField()
    description = models.TextField()
    thumbnail = models.TextField()
    category_tags = models.ManyToManyField(Category, related_name='books')
    user_tags = models.ManyToManyField(UserTag, related_name='books')
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UserBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='userbooks')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='userbooks')
    progress = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title
