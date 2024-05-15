#from django.contrib import admin
from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('add_dojo', views.addDojo),
    path('add_ninja', views.addNinja)
]

