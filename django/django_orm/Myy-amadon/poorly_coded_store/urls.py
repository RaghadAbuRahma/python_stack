from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('checkout_complete/', views.checkout_complete, name='checkout_complete'),
]
