from rest_framework import serializers

from .models import Team, UsersInTeams

from teamfinder_api import serializers as tfapp_serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'owner']
    
class UserInTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersInTeams
        fields = ['user', 'team', 'joinDate']