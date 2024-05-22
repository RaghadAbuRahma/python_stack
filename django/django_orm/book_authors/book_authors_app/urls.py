from django.urls import path
from . import views	
                    
urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<book_id>',views.view_book),
    path('authors', views.index2),
    path('add_authors', views.add_author),
    path('authors/<int:id>', views.view_author),
    path('select_author/<book_id>', views.select_author),
    path('select_book/<author_id>', views.select_book),

]