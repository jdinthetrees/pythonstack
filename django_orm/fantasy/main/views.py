from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Player, Roster
import bcrypt
import random


# class Computer():
#     def __init__(self):
#         # pick three players, and add them to the roster
#         self.addPlayer(somerandomnum)
#     self.roster = Roster()
#     def addPlayer(playerID):
#         self.roster.add(Player.objects.get(id=playerId))
#         # code to add player to roster
#     def reset():
#         #some code to clear out the roster
#         pass

# computer = Computer() # a "computer" that has a roster, and optionally, players already in the rester
# # code for adding human player's pick
# computer.addPlayer()

# def functionToPickPlayer(player_id, roster_id):
#     pass

def index(request):

    if 'user_id' in request.session:
        return redirect('/dashboard')
    context = {
        'all_users': User.objects.all(),
    }

    return render(request, "index.html")

def register(request):
    return render(request, 'registration.html')

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
        name=request.POST['name'],
        email=request.POST['email'],
        password=hashed,
    )
    
    Roster.objects.create(user=user)
    
    
    request.session['user_id'] = user.id
    
    return redirect('/dashboard')

def welcome(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'current_user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, "dashboard.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')

def roster_add(request, player_id):
    user = User.objects.get(id=request.session['user_id'])
    player = Player.objects.get(id=player_id)
    this_roster = user.roster
    if len(this_roster.players.all())<10:
        this_roster.players.add(player)
        player.picked = True  
        player.save()
    
    
    print(user.roster.players.all())
    print(player.name, player.picked)
    return redirect('/draft')

# Create your views here.

def draft_view(request):
    user = User.objects.get(id=request.session['user_id'])
    request.session['lineup'] = ''
    
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'players': Player.objects.all(),
        'roster': user.roster
    }
    
    
    return render(request, 'draft.html', context)

def lineup_view(request):
    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'current_user': user,
        'roster': user.roster,
    }
    
    return render(request, 'lineup.html', context)

def lineup_process(request, player_id):
    id_array = request.session['lineup'].split('|')
    if len(id_array)<=3:
        user = User.objects.get(id=request.session['user_id'])
        player = Player.objects.get(id=player_id)
        request.session['lineup'] += (str(player_id)+'|')
    
    print(request.session['lineup'])
    
    return redirect('/lineup')

def gameplay(request):
    
    print(request.POST)
    id_array = request.POST.getlist('player_id')
    # print(id_array)
    for i in range(0,3,1):
        # print(i, id_array[i])
        if i == 0:
            player1 = Player.objects.get(id=int(id_array[0]))
            points1 = (player1.pts+player1.stl+(player1.ast//2)+(player1.blk//2)+(player1.reb//2))
            random_points1= random.randint(points1 - 5, points1 + 5)
            request.session['points1'] = random_points1
            print(random_points1)
        elif i == 1:
            player2 = Player.objects.get(id=int(id_array[1]))
            points2 = (player2.pts+player2.stl+(player2.ast//2)+(player2.blk//2)+(player2.reb//2))
            random_points2 = random.randint(points2 - 5, points2 + 5)
            request.session['points2'] = random_points2
            print(random_points2)
        else:
            player3 = Player.objects.get(id=int(id_array[2]))
            points3 = (player3.pts+player3.stl+(player3.ast//2)+(player3.blk//2)+(player3.reb//2))
            random_points3= random.randint(points3 - 5, points3 + 5)
            request.session['points3'] = random_points3
            print(random_points3)

        
    total_points = random_points1+random_points2+random_points3
    print(total_points)

    return redirect('/')

# def reset(request):
#     computer.reset()