from django.shortcuts import render
from .models import Book

def home(request):
    return render(request, 'home.html')

def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search)
        if books:
            return render(request, 'books.html', {'books': books, "value": search, "message": "Successfully"})
        else:
            return render(request, 'books.html', {'message': "Not Found"})
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def author(request):
    return render(request, 'author.html')

def book_detail(request, id):
    book = Book.objects.get(id=id)
    if book:
        return render(request, 'book_detail.html', {'book': book})
    else:
        return render(request, 'book_detail.html', {'book': book, "message": "Not Found"})




