
from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return render(request, "index.html")

def get_survey_data(request):
    print(request.POST) # request.POST contains all of the data from the form -> it is a dictionary
    
    form_name=request.POST['name']
    form_location=request.POST['location']
    form_language=request.POST['language']
    form_message=request.POST['message']
    
    return redirect(f"/results/{form_name}/{form_location}/{form_language}/{form_message}")
    
    

def results(request, name, location, language, message):
    context = {
        "name" : name,
        "location" : location,
        "language" : language,
        "message" : message,
    }
    
    return render(request, "results.html", context)


