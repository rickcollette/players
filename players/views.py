from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, GameForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login
import random
import datetime

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'players/register.html', {'success': 'true'})
    else:
        form = UserCreationForm()
    return render(request, 'players/register.html', {'form': form})


def players(request):
    user_list = User.objects.all().order_by('-date_joined')
    page = request.GET.get('page', 1)
    paginator = Paginator(user_list,5)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    
    return render(request,'players/players.html', {'users':users})

def games(request):
    game_list = Game.objects.all().order_by('name')
    page = request.GET.get('page', 1)
    paginator = Paginator(game_list,10)

    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)
    return render(request, 'players/games.html', {'games':games})

@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GameForm()
    return render(request, 'players/add_game.html', {'form':form})
