from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request, "index.html")



def process_money(request):
    if request.POST['location'] == 'farm':
        rand_num = random.randint(10,20)
        request.session['gold'] += rand_num
        # print(request.session['activity_log'])
        # request.session['activity_log'].append(f"Got {rand_num} of gold from the {request.POST['location']}")

    elif request.POST['location'] == 'cave':
        rand_num = random.randint(5,10)
        request.session['gold'] += rand_num
        request.session['activity_log'].append(
            f"Got {rand_num} of gold from the {request.POST['location']}"
            )
    elif request.POST['location'] == 'house':
        rand_num = random.randint(2,5)
        request.session['gold'] += rand_num
        request.session['activity_log'].append(
            f"Got {rand_num} of gold from the {request.POST['location']}"
        )
    elif request.POST['location'] == 'casino':
        rand_num = random.randint(-50,50)
        request.session['gold'] += rand_num
        request.session['activity_log'].append(
            f"Got {rand_num} of gold from the {request.POST['location']}"
        )

    return redirect('/')

# Create your views here.
