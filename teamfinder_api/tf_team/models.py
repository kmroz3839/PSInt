from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class UsersInTeams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    joinDate = models.DateTimeField(default="2000-06-06")