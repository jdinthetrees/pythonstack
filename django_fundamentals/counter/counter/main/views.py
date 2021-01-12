from django.shortcuts import render, HttpResponse, redirect, render_to_response
import random
import datetime
import time
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] +=1
    return render(request, "index.html")



def uptwo(request):
    request.session['counter'] +=1
    return redirect("/")


def destroy(request):
    request.session['counter'] =0
    return redirect("/")


from django.shortcuts import render_to_response
import random
import datetime
import time



def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100


# Create your views here.
