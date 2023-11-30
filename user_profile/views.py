from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from slugify import slugify
from user_profile.models import user_profile

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
        title=title,)
    if request.method == "POST":
        post_info = request.POST
        email = post_info.get('email')
        school_number = post_info.get('number')
        first_name = post_info.get('name')
        last_name = post_info.get('surname')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        if len(school_number) != 9 :
            messages.warning(request, "Lütfen Öğrenci Numaranızı Kontrol Ediniz !")
        if len(password) <= 9 :
            messages.warning(request, "Lütfen şifrenizi en az 9 karakterden oluşturunuz !")
        if password != password_confirm:
            messages.warning(request, "Lütfen şifreyi doğru giriniz !")
            return redirect('sign_up')
        
        user, created = User.objects.get_or_create(username=school_number) 
        if not created:
            messages.warning(request, "Kulübümüze kaydınız bulunmaktadır!")
            return redirect('log_in')
        user.first_name = first_name
        user.last_name = last_name
        user.school_number = school_number
        user.email = email
        user.set_password(password)

        profile, profile_created = user_profile.objects.get_or_create(user=user)

        profile.slug = slugify(f"{first_name}-{last_name}")
        user.save()
        profile.save()

        messages.success(request, f'{user.first_name} sisteme kaydınız gerçekleşti!')
        user_login = authenticate(request, username=school_number, password=password)
        login(request, user_login)
        return redirect(log_in)

    return render(request, 'user/sign_up.html', context)
