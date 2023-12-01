from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.forms import BlogPostModelForm
from blog.models import Category, Tag, BlogPost
import json

@login_required(login_url='user:log_in')
def blog(request):
    blog_title = "Yeni Metin"
    form = BlogPostModelForm()
    context = dict(
        form=form,
        blog_title= blog_title, 
    )

    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None,)
        print(form)
        print(form.errors)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            print(form.cleaned_data)
            f.save()
    return render(request, 'blog_page/blog.html', context)

def blog_page(request):
    blog_title = "Blog"
    context = dict(
        blog_title=blog_title,
        )
    return render(request, 'blog_page/blog_page.html', context)

