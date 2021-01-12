from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt


def index(request):
    if 'user_id' in request.session:
        return redirect('/books')
    context = {
        'all_users': User.objects.all()
    }

    return render(request, "index.html")

def process_user(request):
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
    return redirect('/books')


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
        return redirect('/books')
    messages.error(request, "password does not match try again!")
    return redirect('/')


def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_books': Book.objects.all(),

    }
    return render(request, "welcome.html", context)


def add_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['description'],
        uploaded_by = User.objects.get(id=request.session['user_id']),
    )
    this_book = Book.objects.last()
    this_user = User.objects.get(id=request.session['user_id'])
    this_book.users_who_like.add(this_user)

    print(this_book.users_who_like.all())
    
    return redirect('/books')


def bookedit(request, book_id):
     if 'user_id' != User.objects.get(id=request.session['user_id']):
        return redirect('/books')
    context = {
        'this_book': Book.objects.get(id=book_id),
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, "bookedit.html", context)


    

def logout(request):
    request.session.clear()
    return redirect('/')



# Create your views here.
