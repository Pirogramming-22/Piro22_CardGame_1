from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('game/<int:game_id>/cancel/', views.cancel_game, name='cancel_game'),
    path('game/<int:game_id>/counterattack/', views.counterattack, name='counterattack'),
]