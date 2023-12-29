from rest_framework import serializers

from .models import UserSubmission, GameEntry

class GameEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEntry
        fields = ['id', 'name', 'dataConfigJson']

class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = ['game', 'playername', 'playerurl', 'data1', 'data2', 'data3', 'data4', 'submissiondate']