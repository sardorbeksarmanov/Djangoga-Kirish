from django.shortcuts import render
from .models import Blog, BlogAuthor
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required()
def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {"blogs": blogs})

@login_required()
def blog_detail_view(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_detail.html', {"blog": blog})
