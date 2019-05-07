from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book, Author, Category, UserTag

import json

def index(request):
    return render(request, 'APILibraryApp/index.html')

def saveBook(request):
    if not request.user.is_authenticated:
        return HttpResponse('failure')
    data = json.loads(request.body)
    print(data)
    bookID = data['bookID']
    if Book.objects.filter(bookID = bookID).exists():
        return HttpResponse('already added')
    title = data['title']
    languages = data['languages']
    page_count = data['page_count']
    publish_date = data['publish_date']
    publisher = data['publisher']
    isbn = data['isbn']
    ebook = data['ebook']
    description = data['description']
    thumbnail = data['thumbnail']
    book = Book(bookID=bookID, title=title, languages=languages, page_count=page_count, publish_date=publish_date, publisher=publisher, isbn=isbn, ebook=ebook, description=description, thumbnail=thumbnail)
    book.save()
    book.users.add(request.user)
    author_array = data['authors']
    print(author_array)
    for author in author_array:
        print(author)
        author, created = Author.objects.get_or_create(name=author)
        book.authors.add(author)
    category_array = data['category_tags']
    print(category_array)
    for category in category_array:
        category, created = Category.objects.get_or_create(name=category)
        book.category_tags.add(category)
    return HttpResponse('success')
