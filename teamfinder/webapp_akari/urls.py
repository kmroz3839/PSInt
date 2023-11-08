from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("game/<int:game_id>/", views.game_detail, name="game_detail"),
    path("game/<int:game_id>/submit", views.user_submit, name="user_submit")
]