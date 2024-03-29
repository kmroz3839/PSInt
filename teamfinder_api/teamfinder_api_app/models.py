from django.db import models
from django.contrib.auth.models import User

from tf_auth.models import TFUser

# Create your models here.

class GameEntry(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200, default="")
    dataConfigJson = models.CharField(max_length=2000)

    def __str__(self):
        return self.name + ", Configuration JSON:\n" + self.dataConfigJson 

class UserSubmission(models.Model):
    user = models.ForeignKey(TFUser, on_delete=models.CASCADE, blank=True, null=False)
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

class UserReport(models.Model):
    targetuser = models.ForeignKey(TFUser, related_name='targetuser', on_delete=models.CASCADE, null=False)
    reportinguser = models.ForeignKey(TFUser, related_name='reportinguser', on_delete=models.SET_NULL, null=True)
    details = models.CharField(max_length=2000)

    def __str__(self):
        return f'User report for {self.targetuser.username} from {self.reportinguser.username}: {self.details}'

class GameSuggestion(models.Model):
    name = models.CharField(max_length=100)
    sentByUser = models.ForeignKey(TFUser, on_delete=models.SET_NULL, null=True)
    suggestionCount = models.IntegerField(default=1)