from django.urls import path
from . import views

urlpatterns = [
    path('',  views.index),
    path('get_number', views.get_number),
    path('reset', views.reset),
    # path('too_low', views.too_low),
    # path('too_high', views.too_high),
    # path('you_win', views.you_win)
    
]
