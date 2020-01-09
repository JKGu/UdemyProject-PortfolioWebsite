from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def blogpage(request, blog_id):
    targetblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogpage.html', {'blog':targetblog})