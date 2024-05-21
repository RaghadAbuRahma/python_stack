from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('success', views.new_register),
    path('login', views.login),
    path('logout', views.logout),
]