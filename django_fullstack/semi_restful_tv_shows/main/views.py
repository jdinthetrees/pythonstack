from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show

def index(request):
    print(Show.objects.get(id=6).__dict__)
    for show in Show.objects.all():
        context = {
        'all_the_shows': Show.objects.all(),

    }
    return render(request, "index.html", context)

def showdescription(request, show_id):
    context = {
        'this_show': Show.objects.get(id=show_id),
    }

    return render(request, "showdescription.html", context)

def showedit(request, show_id):
    context = {
        'this_show': Show.objects.get(id=show_id),
    }

    return render(request, "showedit.html", context)

def showupdate(request, show_id):
    errs = Show.objects.show_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values():
            messages.error(request, msg)
        # for key, value in errs.items():
        #     messages.error(request, msg)
        return redirect(f"/shows/{request.POST['this_show.id']}/edit")
    else:
        one_show = Show.objects.get(id=request.POST['this_show.id'])
        one_show.title = request.POST['title']
        one_show.network = request.POST['network']
        one_show.description = request.POST['description']
        one_show.save()
    
    return redirect(f"/shows/{request.POST['this_show.id']}")

def showdelete(request, show_id):
    context = {
        'this_show': Show.objects.get(id=show_id),
    }
    one_show = Show.objects.get(id=request.POST['this_show.id'])
    one_show.delete()
    
    return redirect("/shows")

def shownew(request):

    return render(request, "showadd.html")

def showadd(request):
    print(request.POST)
    errs = Show.objects.show_validator(request.POST)
    if len(errs) > 0:
        for msg in errs.values():
            messages.error(request, msg)
        # for key, value in errs.items():
        #     messages.error(request, msg)
        return redirect(f"/shows/new")
    else:
        Show.objects.create(
        title=request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description'],
    )
    last_show = Show.objects.last().id
    

    return redirect(f"/shows/{last_show}")

# Create your views here.
