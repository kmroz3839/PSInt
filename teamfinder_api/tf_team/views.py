from datetime import datetime

from django.shortcuts import render
from rest_framework import status, permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from teamfinder_api_app.models import GameEntry
from teamfinder_api_app.serializers import GameEntrySerializer

from .models import Team, UsersInTeams
from .serializers import TeamSerializer, UserInTeamSerializer, UserInTeamViewableSerializer, UserInTeamListViewableSerializer

# Create your views here.

class TeamsListAPIView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        gameEntries = Team.objects.all()
        serializer = TeamSerializer(gameEntries, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        gameEntries = Team.objects.filter(mainGame=request.data.get("game"))
        serializer = TeamSerializer(gameEntries, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TeamMembersListAPIView(APIView):
    permission_classes = []

    def get(self, request, targetteam, *args, **kwargs):
        usrobjs = UsersInTeams.objects.filter(team=targetteam)
        serializer = UserInTeamListViewableSerializer(usrobjs, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#
#   USER
#

class UserInTeamsListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        objs = UsersInTeams.objects.filter(user=request.user.id)
        serializer = UserInTeamViewableSerializer(objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request, *args, **kwargs):
        try:
            editTeamEntry = Team.objects.get(id=request.data.get('team'))
            newMainGame = GameEntry.objects.get(id=request.data.get('game'))
            updateTeamEntry = {
                'mainGame': newMainGame.id
            }
            if editTeamEntry.owner.id == request.user.id:
                serializer = TeamSerializer(instance=editTeamEntry, data=updateTeamEntry, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': f'not authorized to edit team {editTeamEntry.id} ({editTeamEntry.owner.id})'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'specified team or game does not exist'}, status=status.HTTP_400_BAD_REQUEST)

class UserJoinTeamAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        obj = Team.objects.filter(id=request.data.get('team'))
        if obj.count() != 0:
            obj = obj.first()
            verifyobj = UsersInTeams.objects.filter(team=obj.id, user=request.user.id)
            if verifyobj.count() == 0:
                newUITEntry = {
                    'user': request.user.id,
                    'team': obj.id,
                    'joinDate': datetime.now()
                }
                serializer = UserInTeamSerializer(data=newUITEntry)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': 'You have already joined this team'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '"team" ID invalid or does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        

class UserRemoveFromTeamAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, targetteam, *args, **kwargs):
        if targetteam is not None:
            try:
                obj = UsersInTeams.objects.get(user=request.user.id, team=targetteam)
                if UsersInTeams.objects.filter(team=targetteam).count() == 1:
                    Team.objects.get(id=targetteam).delete()
                obj.delete()
                return Response({}, status=status.HTTP_200_OK)
            except:
                return Response({'error': 'You do not belong to this team'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'required parameter: "teamid"'}, status=status.HTTP_400_BAD_REQUEST)

class UserCreateTeamAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        newTeamEntry = {
            'owner': request.user.id,
            'name': request.data.get('name')
        }
        serializer = TeamSerializer(data=newTeamEntry, many=False)
        if serializer.is_valid():
            nteamobj = serializer.save()
            rresponse = Response(serializer.data, status=status.HTTP_201_CREATED)
            newUserInTeamEntry = {
                'user': request.user.id,
                'team': nteamobj.id,
                'joinDate': datetime.now()
            }
            usrinteamserializer = UserInTeamSerializer(data=newUserInTeamEntry)
            if usrinteamserializer.is_valid():
                usrinteamserializer.save()
                return rresponse
            else:
                return Response(usrinteamserializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
#   ADMIN
#

class AdminTeamsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class AdminUsersInTeamsView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = UsersInTeams.objects.all()
    serializer_class = UserInTeamSerializer