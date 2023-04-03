from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reservation,CoursPilotage,EcolePilotage

def index(request):
    return render(request, 'index.html')

def reservation_index(request):
    reservations = Reservation.objects.all()
    data = {'reservations':reservations}
    return render(request, 'reservation/index.html', data)

def ecole_index(request):
    ecoles = EcolePilotage.objects.all()
    data = {'ecoles':ecoles}
    return render(request, 'ecole/index.html', data)

def reservation_index_id(request, reservation_id):
    reservation = Reservation.objects.get(id_reservation=reservation_id)
    data = {
        'reservation':reservation,
    }
    return render(request, 'reservation/reservation.html', data)

def ecole_index_id(request, ecole_id):
    ecole = EcolePilotage.objects.get(id_ecole=ecole_id)
    cours = CoursPilotage.objects.filter(id_ecole=ecole_id)
    data = {
        'ecole':ecole,
        'cours':cours,
    }
    return render(request, 'ecole/ecole.html', data)

def auto_index(request):
    cour1 = CoursPilotage.objects.get(id_type= 1)
    cour2 = CoursPilotage.objects.get(id_type= 3)
    cour3 = CoursPilotage.objects.get(id_type= 4)
    data = {
        'coursPilotage1': cour1,
        'coursPilotage2': cour2,
        'coursPilotage3': cour3,
    }
    return render(request, 'automobile/index.html', data)

def avia_index(request):
    cour1 = CoursPilotage.objects.get(id_type=2)
    data = {'coursPilotage1': cour1}
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