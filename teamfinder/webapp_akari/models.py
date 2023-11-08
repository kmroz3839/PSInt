from django.db import models

# Create your models here.

class GameEntry(models.Model):
    name = models.CharField(max_length=200)
    dataConfigJson = models.CharField(max_length=2000)

    def __str__(self):
        return self.name + ", Configuration JSON:\n" + self.dataConfigJson 

class UserSubmission(models.Model):
    game = models.ForeignKey(GameEntry, on_delete=models.CASCADE)
    playername = models.CharField(max_length=100)
    playerurl = models.CharField(max_length=150)
    data1 = models.IntegerField(default=0)
    data2 = models.IntegerField(default=0)
    data3 = models.IntegerField(default=0)
    data4 = models.IntegerField(default=0)

    def __str__(self):
        return f"Game: {self.game.name}, Player name: {self.playername}, Player URL: {self.playerurl}, {self.data1}|{self.data2}|{self.data3}|{self.data4}"