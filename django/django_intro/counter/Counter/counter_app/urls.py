from django.urls import path     
from . import views
urlpatterns = [
    path('', views.counter), 
    path('destroy_session', views.destroySession),
    path('destroy_session', views.reset),
    path('submitt', views.submitt),
]
