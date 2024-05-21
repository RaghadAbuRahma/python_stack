from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money', views.processMoney),
    path('increase_decrease', views.quest),
    path('clear', views.clear),
    path('indenx', views.index)

]