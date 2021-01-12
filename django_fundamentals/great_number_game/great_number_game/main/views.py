from django.shortcuts import render, redirect
import random

def index(request):
    if 'random' not in request.session:
        request.session['random'] = random.randint(1, 100)
    print('this is the random number ', request.session['random'])
    return render(request, "index.html")

def get_number(request):
    request.session['guess'] = request.POST['number']
    print("this is a guess ", request.session['guess'])

            
    if int(request.session['guess'])< int(request.session['random']):
        request.session['message'] = 'too low'
    elif int(request.session['guess'])> int(request.session['random']):
        request.session['message'] = 'too high'
    else:
        request.session['message'] = 'you win'
    return redirect("/")

def reset(request):
    del request.session['guess']
    del request.session['message']
    return redirect("/")



# Create your views here