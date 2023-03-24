from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('reservation/',views.reservation_index, name='reservation_index'),
]
