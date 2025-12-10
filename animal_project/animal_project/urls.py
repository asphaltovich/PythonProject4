
from django.contrib import admin
from django.urls import path
from animals.views import mammal_list, bird_list

urlpatterns = [
    path('mammals/', mammal_list, name="mammal_list"),
    path('birds/', bird_list, name="bird_list"),
]
