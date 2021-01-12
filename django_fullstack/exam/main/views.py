from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Job
import bcrypt

def index(request):

    if 'user_id' in request.session:
        return redirect('/dashboard')
    context = {
        'all_users': User.objects.all(),
    }

    return render(request, "index.html")

def process_user(request):

    if 'user_id' in request.session:
        return redirect('/dashboard')
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')

    password = request.POST['password']
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    # print(password, "\n", hashed )
    user = User.objects.create(
        f_name=request.POST['f_name'],
        l_name=request.POST['l_name'],
        email=request.POST['email'],
        password=hashed,
    )
    request.session['user_id'] = user.id
    return redirect('/dashboard')

def login_user(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/')
    email_users = User.objects.filter(email=request.POST['email'])
    
    our_user = email_users[0]
    if bcrypt.checkpw(request.POST['password'].encode(), our_user.password.encode()):
        request.session['user_id'] = our_user.id
        return redirect('/dashboard')
    messages.error(request, "password does not match try again!")
    return redirect('/')


def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_jobs': Job.objects.all(),
        # 'this_job': Job.objects.get(id=job_id),
        # 'all_my_jobs': 

    }
    # item = Job.objects.get(id=job_id)
    # if request.user == item.user:
    #     Job.objects.filter(id=job_id).delete()
    #     return redirect('/dashboard')

    return render(request, "dashboard.html", context)

def newjob(request):
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, "newjob.html", context)

def add_job(request):
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/jobs/new')

    Job.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
        location = request.POST['location'],
        uploaded_by = User.objects.get(id=request.session['user_id']),
    )
    this_job = Job.objects.last()
    this_user = User.objects.get(id=request.session['user_id'])
    this_job.users.add(this_user)

    # print(Job.objects.last())
    
    return redirect('/dashboard')

def jobedit(request, job_id):
    
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'this_job': Job.objects.get(id=job_id),
    }

    return render(request, "jobedit.html", context)


def jobupdate(request, job_id):
    
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect(f"/jobs/edit/{request.POST['this_job.id']}")
    else:
        one_job = Job.objects.get(id=request.POST['this_job.id'])
        one_job.title = request.POST['title']
        one_job.location = request.POST['location']
        one_job.description = request.POST['description']
        one_job.save()
    
    return redirect("/dashboard")

def viewjob(request, job_id):
    
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'this_job': Job.objects.get(id=job_id),
    }

    return render(request, "viewjob.html", context)

def jobdelete(request, job_id):
    # context = {
    #     'this_job': Job.objects.get(id=job_id),
    # }
    # one_job= Job.objects.get(id=request.POST['this_job.id'])
    # one_job.delete()

    job_to_delete = Job.objects.get(id=job_id)
    job_to_delete.delete()
    
    return redirect("/dashboard")




def logout(request):
    request.session.clear()
    return redirect('/')


# Create your views here.
