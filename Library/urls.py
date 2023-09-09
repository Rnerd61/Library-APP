from django.urls import path, include
from .views import *
urlpatterns = [
    path('books', BooksView.as_view()),
    path('books/<int:id>', BooksView.as_view()),
    path('author', AuthorView.as_view()),
    path('author/<int:id>', AuthorView.as_view()),
]