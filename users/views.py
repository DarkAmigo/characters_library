from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('character_list')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

