from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_user', views.process_user),
    path('login_user', views.login_user),
    path('success', views.welcome),
    path('message', views.message),
    path('comment', views.comment),
    path('logout', views.logout)
]
