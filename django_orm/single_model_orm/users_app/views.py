from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    for user in User.objects.all():
        print(user.__dict__)
    context = {
        'all_the_users': User.objects.all()
    }
    return render(request, "index.html", context)


def process(request):
    User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email'],
        age=request.POST['age'],
        )

    print(request.POST)
    return redirect('/')

# Create your views here.
