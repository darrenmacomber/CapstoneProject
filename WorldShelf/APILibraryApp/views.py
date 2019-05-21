from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Book, Author, Category, UserTag, UserBook, UserComment
from ProfileApp.views import makeComment

import json

def index(request):
    return HttpResponse('ok')

def bookSearch(request):
    return render(request, 'APILibraryApp/bookSearch.html')

def tagSearch(request):
    return render(request, 'APILibraryApp/tagSearch.html')

def saveBook(request):
    if not request.user.is_authenticated:
        return HttpResponse('failure')
    data = json.loads(request.body)
    bookID = data['bookID']
    if Book.objects.filter(bookID = bookID).exists():
        target_book = Book.objects.get(bookID = bookID)
        if target_book.userbooks.filter(user = request.user).exists():
            return HttpResponse('already added')
        else:
            user = request.user
            userbook = UserBook(user=user, book=target_book, progress=0)
            userbook.save()
            return HttpResponse('success')
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
    author_array = data['authors']
    for author in author_array:
        author, created = Author.objects.get_or_create(name=author)
        book.authors.add(author)
    category_array = data['category_tags']
    for category in category_array:
        category, created = Category.objects.get_or_create(name=category)
        book.category_tags.add(category)
    user = request.user
    userbook = UserBook(user=user, book=book, progress=0)
    userbook.save()
    return HttpResponse('success')

def getUserBooks(request):
    indata = json.loads(request.body)
    target_user = indata['user']
    userbooks = UserBook.objects.all()
    data = {'userbooks': []}
    for userbook in userbooks:
        id = userbook.id
        book = userbook.book.bookID
        user = userbook.user.username
        progress = userbook.progress
        if user == target_user:
            data['userbooks'].append({
                'id': id,
                'book': book,
                'progress': progress,
                })
    return JsonResponse(data)

def getTags(request):
    data = {'tags': []}
    tag_array = UserTag.objects.all()
    for tag in tag_array:
        name = tag.name
        data['tags'].append({
            'name': name,
        })
    return JsonResponse(data)

def findTaggedBooks(request):
    indata = json.loads(request.body)
    target_tag = indata['target_tag']
    data = {'bookIDs': []}
    book_array = Book.objects.all()
    for book in book_array:
        for tag in book.user_tags.all():
            if tag.name == target_tag:
                data['bookIDs'].append({
                    'bookID': book.bookID
                })
    return JsonResponse(data)

def bookTags(request):
    bookID = request.GET['bookID']
    data = {'UserTag': []}
    if Book.objects.filter(bookID = bookID).exists():
        target_book = Book.objects.get(bookID = bookID)
        for tag in target_book.user_tags.all():
            data['UserTag'].append(tag.name)
    return JsonResponse(data)

def saveTags(request):
    if not request.user.is_authenticated:
        return HttpResponse('failure')
    data = json.loads(request.body)
    bookID = data['bookID']
    name = data['tag']
    target_tag = UserTag.objects.get(name=name)
    if Book.objects.filter(bookID = bookID).exists():
        target_book = Book.objects.get(bookID = bookID)
        if target_book.user_tags.filter(name=name).exists():
            return HttpResponse('already added')
        target_book.user_tags.add(target_tag)
        target_book.save()
        return HttpResponse('success')
