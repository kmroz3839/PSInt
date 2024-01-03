from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Team
from .serializers import TeamSerializer

# Create your views here.

class TeamsListAPIView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        gameEntries = Team.objects.all()
        serializer = TeamSerializer(gameEntries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)