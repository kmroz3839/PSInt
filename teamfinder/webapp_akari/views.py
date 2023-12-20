from django.shortcuts import render
from django.template import loader
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count
import json

from .models import GameEntry, UserSubmission

# Create your views here.
def index(request):
    #template = loader.get_template("akari/mainpage.html")
    #return HttpResponse(template.render({}, request))
    return render(request, "akari/mainpage.html", {})

def akari_logout(request):
    auth.logout(request)
    #return HttpResponseRedirect("/")
    return render(request, "registration/logout.html", {})

class GameListEntry:
    num: int
    name: str
    id: int
    def __init__(self, num, name, id):
        self.num = num
        self.name = name
        self.id = id

def games_list(request):
    gameStats = sorted([GameListEntry(num=UserSubmission.objects.filter(game_id=x.id).count(), name=x.name, id=x.id) for x in GameEntry.objects.all()], key= lambda x: x.num)[::-1]

    return render(request, "akari/gamelist.html", {
        "gamelist": gameStats
    })

def game_detail(request, game_id):
    try:
        game = json.loads(GameEntry.objects.filter(id=game_id).first().dataConfigJson)
        gameUserSubmissions = UserSubmission.objects.filter(game=game_id)
        dataFields = {x:{y:game[x][y] for y in game[x]} for x in game if x.startswith("data")}
        #print(game)
        print(dataFields)
        print(gameUserSubmissions)

        return render(request, "akari/gamedetails.html", {
            "recentusers": gameUserSubmissions,
            "game": {
                "name": game["name"],
                "hasUserLink": game["hasPlayerURL"],
                "nDataFields": game["nDataFields"],
                "dataFields": dataFields,
                "jsonConf": game
            }
        })
    except RuntimeError:
        return render(request, "akari/errorpage.html", {})

def user_submit(request, game_id):
    return HttpResponse(f"[akari] Submitting user's details for {game_id}")