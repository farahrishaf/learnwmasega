from django.urls import path
from belajar import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('belajar', views.belajar, name='belajar') 
]