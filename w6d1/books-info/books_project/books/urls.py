from django.urls import path
from . import views

urlpatterns = [
    path('list-books/', views.list_books, name='list_books'),
    path('book-detail/<int:id>/', views.book_detail, name='book_detail'),
    path('create-book/', views.create_book, name='create_book'),
]
