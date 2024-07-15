from django.urls import path
from .views import home, books, book_detail
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('books/<int:id>', book_detail, name='book_detail'),
    path('account/', views.account, name='account'),

]