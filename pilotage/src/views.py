from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reservation,CoursPilotage

def index(request):
    return render(request, 'index.html')

def reservation_index(request):
    reservations = Reservation.objects.all()
    data = {'reservations':reservations}
    return render(request, 'reservation/index.html', data)

def reservation_index_id(request, reservation_id):
    reservation = Reservation.objects.get(id_reservation=reservation_id)
    data = {
        'reservation':reservation,
    }
    return render(request, 'reservation/reservation.html', data)

def auto_index(request):
    cours = CoursPilotage.objects.all()
    data = {'cours':cours}
    return render(request, 'automobile/index.html', data)

def avia_index(request):
    cours = CoursPilotage.objects.all()
    data = {'cours': cours}
    return render(request, 'aviation/index.html', data)

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