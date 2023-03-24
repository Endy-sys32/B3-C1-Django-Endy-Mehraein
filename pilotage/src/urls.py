from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('reservation/',views.reservation_index, name='reservation_index'),
    path('automobile/',views.auto_index, name='auto_index'),
    path('aviation/',views.avia_index, name='avia_index'),
    path('compte/',views.compte_index, name='compte_index'),
]
