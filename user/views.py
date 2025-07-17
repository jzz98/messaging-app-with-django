from django.shortcuts import render, HttpResponse, redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def singup(request):
    if request.method == 'POST':
        try:
            data = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            data.save()
            return redirect('login')
        except IntegrityError:
            return render(request, 'register.html', {'error': "Cuenta existente"})
    else:
        return render(request, 'register.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
            if user is None:
                return render(request, 'login.html', {'error': 'Credenciaeles incorrectas'})

            login(request, user)
            return redirect('chat')
        
        except IntegrityError:
            return render(request, 'login.html', {'error': 'Usuario no existe'})
