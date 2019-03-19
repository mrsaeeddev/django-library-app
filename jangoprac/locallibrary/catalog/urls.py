from django.urls import path
from catalog.views import index, books, book_detail, authors, author_detail

urlpatterns = [
    path('',index, name='index'),
    path('books/', books, name='books'),
    path('book/<int:pk>', book_detail , name="book_detail"),
    path('authors/', authors, name="authors"),
    path('author/<int:pk>', author_detail ,name="author_detail"),
]