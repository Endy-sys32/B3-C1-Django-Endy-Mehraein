from django.db import models

class TypePilotage(models.Model):
    id_type = models.IntegerField(primary_key=True)
    libelle_pilotage = models.CharField(max_length=200)

    def __str__(self):
        return self.libelle_pilotage

class VehiculePilotage(models.Model):
    id_vehicule = models.IntegerField(primary_key=True)
    marque_vehicule = models.CharField(max_length=200)
    model_vehicule = models.CharField(max_length=400)

    def __str__(self):
        return self.model_vehicule

class CoursPilotage(models.Model):
    id_cours = models.IntegerField(primary_key=True)
    id_type = models.ForeignKey(TypePilotage, on_delete=models.CASCADE)
    id_vehicule = models.ForeignKey(VehiculePilotage, on_delete=models.CASCADE)

class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    nom_user = models.CharField(max_length=200)
    prenom_user = models.CharField(max_length=300)
    login_user = models.CharField(max_length=400)
    password_user = models.CharField(max_length=300)

    def __str__(self):
        return self.nom_user

class Reservation(models.Model):
    id_reservation = models.IntegerField(primary_key=True)
    cours = models.ForeignKey(CoursPilotage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_reservation = models.DateField()
    heure_deb_reservation = models.DateTimeField()
    heure_fin_reservation = models.DateTimeField()

