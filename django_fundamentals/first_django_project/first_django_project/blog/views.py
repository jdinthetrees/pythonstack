from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect('/blogs')

def new(request):
    return HttpResponse("placeholder to later display a new form to create a new blog")

def show(request, number):
    pass 
    return HttpResponse(f"placeholder to display a blog number: {number}")

def create(request):
    return redirect('/')

def edit(request, number):
    pass
    return HttpResponse(f"placeholder to edit blog {number}")


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def destroy(request, number):
    pass
    return redirect('/blogs')




# Create your views here.
