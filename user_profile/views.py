from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home_page(request):
    title = "Anasayfa"
    context = dict(
        title=title,
        )
    return render(request, 'homepage/homepage.html', context)

def log_in(request):
    #Giriş yapan kullanıcının direkt sayfaya yönlendirilmesi için aşağıdaki if bloğunu kullandım.
    if request.user.is_authenticated:
        messages.info(request, f' {request.user.username} Önceden giriş yaptınız.')
        return redirect('blog_page')
    title = "Giriş Yap"
    context = dict(
        title=title,
        )
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if len(username) != 9:
            messages.warning(request, f'Lütfen Bilgilerinizi Doğru Giriniz!')
            return redirect('log_in')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f' {request.user.username} Hoşgeldiniz!')
            return redirect('blog_page')
        
    return render(request, 'user/log_in.html', context)

def log_out(request):
    messages.success(request, f' {request.user.username} Oturumunuz Kapatıldı!')
    logout(request)
    return redirect('home')

def sign_up(request):
    title = "Üye Ol"
    context = dict(
        title=title,
        )
    if request.method == 'POST':
        post_info = request.POST
        email = post_info.get('email')
        name = post_info.get('name')
        department = post_info.get('department')
        number = post_info.get('number')
        phone_number = post_info.get('phone_number')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        print(request.POST)
    return render(request, 'user/sign_up.html', context)
