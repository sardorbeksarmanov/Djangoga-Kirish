from django.contrib import admin
from .models import Author, Book, Comment, PurchasedBook, Wishlist
from import_export.admin import ImportExportModelAdmin


admin.site.register(PurchasedBook)
admin.site.register(Wishlist)
@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'created_at')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'author', 'price', 'count', 'created_at')
    list_display_links = ('id', 'title', 'slug', 'description', 'author')
    search_fields = ('id', 'title', 'slug', 'author__first_name', 'author__last_name')
    ordering = ('title', 'author')
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'book', 'text', 'created_at')
    list_display_links = ('id', 'user', 'book')
    search_fields = ('id', 'user__username', 'book__title', 'text')
    ordering = ('created_at', )
