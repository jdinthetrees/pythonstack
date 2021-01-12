from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_user', views.process_user),
    path('login_user', views.login_user),
    path('dashboard', views.welcome),
    path('jobs/new', views.newjob),
    path('jobs/create', views.add_job),
    path('jobs/<int:job_id>', views.viewjob),
    path('jobs/edit/<int:job_id>', views.jobedit),
    path('jobs/edit/<int:job_id>/update', views.jobupdate),
    path('jobs/destroy/<int:job_id>', views.jobdelete),
    path('logout', views.logout),
]
