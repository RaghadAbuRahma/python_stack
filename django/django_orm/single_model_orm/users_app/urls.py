from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('processe', views.prosesse),
]
