from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def reservation_index(request):
    return render(request, 'reservation/index.html')

def auto_index(request):
    return render(request, 'automobile/index.html')

def avia_index(request):
    return render(request, 'aviation/index.html')

def compte_index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect."
    else:
        message = ""
    return render(request, 'compte/index.html', {'message': message})