from django.urls import path     
from . import views
urlpatterns = [
    path('', views.randomNum),	
    path('compare', views.compare),
]

