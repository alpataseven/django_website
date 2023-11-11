from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    title = "Anasayfa"
    context = dict(
        title=title,
        )
    return render(request, 'homepage/homepage.html', context)

def log_in(request):
    title = "Giriş Yap"
    context = dict(
        title=title,
        )
    return render(request, 'homepage/log_in.html', context)

def sign_up(request):
    title = "Üye Ol"
    context = dict(
        title=title,
        )
    return render(request, 'homepage/sign_up.html', context)

