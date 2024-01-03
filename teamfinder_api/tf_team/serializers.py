from rest_framework import serializers

from .models import Team, UsersInTeams

from teamfinder_api_app.serializers import GameEntrySerializer

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'owner', 'mainGame']
    
class UserInTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersInTeams
        fields = ['user', 'team', 'joinDate']


#
#   USER MODE SERIALIZERS
#

class TeamViewableSerializer(serializers.ModelSerializer):
    mainGame = GameEntrySerializer()
    class Meta:
        model = Team
        fields = ['id', 'name', 'owner', 'mainGame']

class UserInTeamViewableSerializer(serializers.ModelSerializer):
    team = TeamViewableSerializer()
    class Meta:
        model = UsersInTeams
        fields = ['user', 'team', 'joinDate']