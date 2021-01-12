from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('process_user', views.process_user),
    path('login_user', views.login_user),
    path('books', views.welcome),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.bookedit),
    path('logout', views.logout),
]
