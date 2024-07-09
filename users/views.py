from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html', {'message': 'Foydalanuvchi topilmadi.'})

    return render(request, 'auth/login.html')

def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if password != password2:
            return render(request, 'auth/register.html', {'message': 'Parollar mos emas.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {'message': 'Bunday foydalanuvchi allaqachon mavjud.'})

        new_user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        new_user.save()
        return redirect('login')

    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    return redirect('home')