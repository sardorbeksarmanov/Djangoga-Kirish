from django.db import models
from django.utils import timezone
from book.models import Author

class BlogAuthor(models.Model):
    full_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog/author/')
    created = models.DateTimeField(auto_now_add=True)  # 'auto_now_add' to'g'ri ishlatilgan

    def __str__(self):
        return self.full_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)  # Blog modeliga 'image' qo'shildi
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

