from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

def login_view(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('index'))
    else:
        return render(request, 'authentication/login-form.html')

    return render(request, 'authentication/login-form.html')

def logout_view(request):

    if request.user.is_authenticated():
        logout(request)
    else:
        return redirect(reverse('login'))

    return redirect(reverse('index'))
