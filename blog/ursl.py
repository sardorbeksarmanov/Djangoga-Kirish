from django.urls import path
from .views import blog_list_view, blog_detail_view

urlpatterns = [
    path('blog/', blog_list_view, name='blog'),
    path('blog/<int:id>/', blog_detail_view, name='blog-detail'),
]