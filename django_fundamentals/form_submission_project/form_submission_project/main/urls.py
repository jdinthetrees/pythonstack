from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('get_survey_data', views.get_survey_data),
    path('results/<name>/<location>/<language>/<message>', views.results),
]
#remember to take front slash away from url path, and tht redirect path 'get_survey_data
#is a phantom path but necessary