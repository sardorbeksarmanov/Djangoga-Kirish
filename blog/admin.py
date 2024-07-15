from django.contrib import admin
from .models import BlogAuthor, Blog

admin.site.register([Blog, BlogAuthor])
