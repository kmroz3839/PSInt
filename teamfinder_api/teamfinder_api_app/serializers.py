from rest_framework import serializers

from .models import UserSubmission, GameEntry, UserReport

class GameEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameEntry
        fields = ['id', 'name', 'dataConfigJson']

class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = ['user', 'game', 'playername', 'playerurl', 'data1', 'data2', 'data3', 'data4', 'submissiondate']

class UserReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReport
        fields = ['targetuser', 'reportinguser', 'details']