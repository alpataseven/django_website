from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    blog_title = "Blog"
    context = dict(
        blog_title= blog_title,
        )
    return render(request, 'blog_page/blog.html', context)

def blog_page(request):
    blog_title = "Yeni Metin"
    context = dict(
        blog_title=blog_title,
        )
    return render(request, 'blog_page/blog_page.html', context)

