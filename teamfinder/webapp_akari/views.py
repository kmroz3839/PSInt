from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("[akari] index page")

def game_detail(request, game_id):
    return HttpResponse(f"[akari] Viewing details for {game_id}")

def user_submit(request, game_id):
    return HttpResponse(f"[akari] Submitting user's details for {game_id}")