from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def reservation_index(request):
    return render(request, 'reservation/index.html')