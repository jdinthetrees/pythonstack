# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('shows', views.index),
    path('shows/<int:show_id>', views.showdescription),
    path('shows/<int:show_id>/edit', views.showedit),
    path('shows/<int:show_id>/update', views.showupdate),
    path('shows/<int:show_id>/destroy', views.showdelete),
    path('shows/new', views.shownew),
    path('shows/create', views.showadd),
]
