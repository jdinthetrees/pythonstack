from django.urls import path     
from . import views
urlpatterns = [
    path('', views.demo_piechart),
    # path('uptwo', views.uptwo),
    # path('destroy_session', views.destroy),	   
]

