from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.players, name = 'home'),
    path('register/', views.register, name='user_register'),
    path('accounts/', include('django.contrib.auth.urls'), name='user_login'),
    path('games/', views.games, name = 'games'),
    path('', views.players, name = 'players'),
    path('add_game/', views.add_game, name = 'add_game'),
]