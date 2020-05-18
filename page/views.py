from django.shortcuts import render
from game.models import Game

def index(request):
    return render(request, 'page/index.html', locals())

def lk(request):
    if request.user.is_authenticated:
        allGames = Game.objects.filter(player=request.user)
        user = request.user
        return render(request, 'page/lk.html', locals())
    else:
        return render(request, 'page/index.html', locals())