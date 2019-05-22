from django.db import models
from django.contrib.auth.models import User

'''Tracks Authors created with Book instances'''
# Will be used for an Author-based User search at a later date.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

'''Displays Categories with proper grammar in Admin'''
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

'''Simple tags that track User impressions'''
# UserTags only contain names and can only be created by Admin currently.
# Correlate to ManyToManyField on the Book instance in question.
class UserTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

'''Represents a Book, once added to the shelf, taking info from API'''
# API provides data to fill model parameters.
# Empty ManyToManyField for user tags, which are applied after creation.
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

'''Represents the relationship between User and Book'''
# Tracks the Book and Users as models/related name on respective models.
# Tracks progress by number of pages.
class UserBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='userbooks')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='userbooks')
    progress = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title

'''Comments placed on Books'''
# Tracks Book the comment was made on, User who made the Comment, and comment text.
# Tracks Progress Point in pages for purposes of the Spoiler Protection function.
# Dates are extracted strings made from datetime objects.
class UserComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments')
    text = models.TextField()
    progress_point = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def prettycreatedate(self):
        converted = self.date_edited.strftime('%B %d, %Y')
        return converted

    def prettyeditdate(self):
        converted = self.date_edited.strftime('%B %d, %Y')
        return converted

    def __str__(self):
        return 'UserComment('+ str(self.id) +'):' + self.book.title + ', ' + self.user.username
