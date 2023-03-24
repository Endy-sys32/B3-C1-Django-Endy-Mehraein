from django.shortcuts import render
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
    return render(request, 'compte/index.html')