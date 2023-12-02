from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.forms import BlogPostModelForm
from django.utils import timezone
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
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value').lower())
                tag_item.is_active = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request, "Gönderiniz Başarıyla Kaydedildi.!")
            return redirect('blog_page')
            
    return render(request, 'blog_page/blog.html', context)

def blog_page(request):
    blog_title = "Blog"
    posts = BlogPost.objects.filter(is_active=True)
    top_posts = posts.order_by('-view_count')[:6]
    tags = Tag.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    my_objects = BlogPost.objects.all()
    context = dict(
        blog_title = blog_title,
        categories=categories,
        posts=posts,
        tags=tags,
        my_objects=my_objects,
        current_time=timezone.now()
        )
    return render(request, 'blog_page/blog_page.html', context)

