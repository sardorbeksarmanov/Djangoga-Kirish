from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Book, Author, PurchasedBook, Wishlist

def home(request):
    return render(request, 'home.html')

@login_required()
def books(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search)
        if books.exists():
            return render(request, 'books.html', {'books': books, 'value': search, 'message': 'Successfully'})
        else:
            return render(request, 'books.html', {'message': 'Not Found'})
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def authors(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

def account(request):
    purchased_books = PurchasedBook.objects.filter(user=request.user)
    wishlist_books = Wishlist.objects.filter(user=request.user)
    context = {
        'purchased_books': purchased_books,
        'wishlist_books': wishlist_books,
    }
    return render(request, 'account.html', context)