from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GameEntry(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200, default="")
    dataConfigJson = models.CharField(max_length=2000)

    def __str__(self):
        return self.name + ", Configuration JSON:\n" + self.dataConfigJson 

class UserSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    game = models.ForeignKey(GameEntry, on_delete=models.CASCADE)
    playername = models.CharField(max_length=100)
    playerurl = models.CharField(max_length=150)
    data1 = models.IntegerField(default=0)
    data2 = models.IntegerField(default=0)
    data3 = models.IntegerField(default=0)
    data4 = models.IntegerField(default=0)
    submissiondate = models.DateTimeField(default="2000-06-06")

    def __str__(self):
        return f"[{self.submissiondate}] Game: {self.game.name}, Player name: {self.playername}, Player URL: {self.playerurl}, {self.data1}|{self.data2}|{self.data3}|{self.data4}"

class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class UsersInTeams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    joinDate = models.DateTimeField(default="2000-06-06")

class UserReport(models.Model):
    targetUser = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    reportingUser = models.ForeignKey(User, related_name='reportingUser', on_delete=models.SET_NULL, null=True)
    details = models.CharField(max_length=2000)

class GameSuggestion(models.Model):
    name = models.CharField(max_length=100)
    sentByUser = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)