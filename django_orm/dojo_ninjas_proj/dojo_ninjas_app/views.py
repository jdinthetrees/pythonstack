from django.shortcuts import render, HttpResponse, redirect
from . import views
from .models import Dojo, Ninja


def index(request):
    # print(Dojo.objects.all())
    context = {
        'all_the_dojos': Dojo.objects.all(),
        'all_the_ninjas': Ninja.objects.all()
    }
    return render(request, "index.html", context)

def process(request):

    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )

    return redirect('/')

def process_student(request):
    # print("*******************", request.POST)

    this_dojo=Dojo.objects.get(id=request.POST['dojo_ID'])

    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo=this_dojo,
        
    )

    return redirect('/')



# Create your views here.

