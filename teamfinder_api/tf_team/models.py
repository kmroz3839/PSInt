from django.db import models
from django.contrib.auth.models import User

from teamfinder_api_app.models import GameEntry

class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    mainGame = models.ForeignKey(GameEntry, on_delete=models.SET_NULL, null=True, default=None)

class UsersInTeams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    joinDate = models.DateTimeField(default="2000-06-06")