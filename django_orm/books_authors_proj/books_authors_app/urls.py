from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('books/<int:book_id>', views.books),
    path('booksaddauthor', views.booksaddauthor), 
    path('authors', views.author),
    path('addauthorprocess', views.addauthor_process),
    path('authors/<int:author_id>', views.authors),
    path('authoraddsbook', views.authoraddsbook)
]