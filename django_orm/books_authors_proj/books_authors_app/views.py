from django.shortcuts import render, HttpResponse, redirect
from . import views
from .models import Author, Book

def index(request):
    # print(Author.objects.all())
    #for book in Book.objects.all():
    context = {
        'all_the_authors': Author.objects.all(),
        'all_the_books': Book.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['description'],
    )
    return redirect('/')

def books(request, book_id):
    context = {
        'all_the_authors': Author.objects.all(),
        'this_book': Book.objects.get(id=book_id),
    }
    
    return render(request, "books.html", context)

def booksaddauthor(request):
    one_book = Book.objects.get(id=request.POST['this_book.id'])
    one_author = Author.objects.get(id=request.POST['author.id'])
    one_author.books.add(one_book)
    return redirect(f"/books/{request.POST['this_book.id']}")

def author(request):
    context = {
        'all_the_authors': Author.objects.all(),
        'all_the_books': Book.objects.all()
    }

    return render(request, "addauthor.html", context)

def addauthor_process(request):
    print(Author.objects.all())
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes'],
    )
    return redirect('/authors')

def authors(request, author_id):

    context = {
        'all_the_authors': Author.objects.all(),
        'all_the_books': Book.objects.all(),
        'this_author': Author.objects.get(id=author_id)
    }
    return render(request, "displayauthor.html", context)

def authoraddsbook(request):
    one_book = Book.objects.get(id=request.POST['book.id'])
    one_author = Author.objects.get(id=request.POST['author.id'])
    one_author.books.add(one_book)
    return redirect(f"/authors/{request.POST['author.id']}")


# Create your views here.
