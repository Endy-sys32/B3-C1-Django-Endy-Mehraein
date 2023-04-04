from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('reservation/',views.reservation_index, name='reservation_index'),
    path('reservation/<int:reservation_id>/',views.reservation_index_id, name='reservation_index_id'),
    path('reservation/reserver/<int:cours_id>/',views.reserver_cours_id, name='reserver_cours_id'),
    path('automobile/',views.auto_index, name='auto_index'),
    path('aviation/',views.avia_index, name='avia_index'),
    path('compte/',views.compte_index, name='compte_index'),
    path('ecole/',views.ecole_index, name='ecole_index'),
    path('ecole/<int:ecole_id>/',views.ecole_index_id, name='ecole_index_id'),
    path('ecole/<int:ecole_id>/<int:cours_id>/',views.cour_ecole_index, name='cour_ecole_index'),
]