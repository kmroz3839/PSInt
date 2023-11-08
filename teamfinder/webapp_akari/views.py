from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    #template = loader.get_template("akari/mainpage.html")
    #return HttpResponse(template.render({}, request))
    return render(request, "akari/mainpage.html", {})

def game_detail(request, game_id):
    return HttpResponse(f"[akari] Viewing details for {game_id}")

def user_submit(request, game_id):
    return HttpResponse(f"[akari] Submitting user's details for {game_id}")