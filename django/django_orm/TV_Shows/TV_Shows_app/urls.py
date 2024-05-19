from django.urls import path     
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.new_show),
    path('create', views.create_show),
    path('show/<id>', views.view_show),
    path('show/<id>/edit', views.edit),
    path('show/<id>/destroy',views.delete),
    path('back', views.back),
    path('show/<id>/update', views.update),
]