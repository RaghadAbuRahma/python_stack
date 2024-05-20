from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<id>',views.view_book),
    path('authors', views.index2),
    path('add_authors', views.add_author),
    path('authors/<id>', views.view_author),
    path('select_author', views.select_author),

]