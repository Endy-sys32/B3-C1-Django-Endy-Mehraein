from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation


class CreateReservation(UserCreationForm):
    cours = forms.CharField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    date_reservation = forms.DateField(required=True, help_text='Required.')
    heure_deb_reservation = forms.DateTimeField(required=True, help_text='Required.')
    heure_fin_reservation = forms.DateTimeField(required=True, help_text='Required.')
    class Meta:
        model = Reservation
        fields = ('id_reservation', 'cours', 'user', 'date_reservation', 'heure_deb_reservation', 'heure_fin_reservation')
