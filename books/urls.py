from django.urls import path
from . import views

urlpatterns = [
    path('browse/', views.browse_books, name='browse_books'),
    path('add/', views.add_book, name='add_book'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
