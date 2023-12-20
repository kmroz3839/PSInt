from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("app_logout", views.app_logout, name="app_logout"),
    path("games", views.games_list, name="games_list"),
    path("game/<int:game_id>/", views.game_detail, name="game_detail"),
    path("game/<int:game_id>/submit", views.user_submit, name="user_submit")
]