from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form_register_user = UserRegisterForm(request.POST)
        if form_register_user.is_valid():
            username = form_register_user.cleaned_data['username']
            email = form_register_user.cleaned_data['email']
            password = form_register_user.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                form_register_user.add_error('username', 'Пользователь с таким именем уже существует.')

            elif User.objects.filter(email=email).exists():
                form_register_user.add_error('email', 'Пользователь с таким email уже существует.')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('new:home')
                    return redirect('new:home')

    else:
        form_register_user = UserRegisterForm()

    context = {'form_register_user': form_register_user}
    return render(request, 'user_app/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('new:home')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('new:home')
    else:
        form = AuthenticationForm()

    return render(request, 'user_app/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'user_app/home.html', {'user': request.user})


