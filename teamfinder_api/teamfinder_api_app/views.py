import datetime
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import GameEntry, UserSubmission
from .serializers import GameEntrySerializer, UserSubmissionSerializer

import json

# Create your views here.

class GameEntryListApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        gameEntries = GameEntry.objects.all()
        serializer = GameEntrySerializer(gameEntries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GameEntryRankingListApiView(APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        d = {}
        for x in GameEntry.objects.all():
            d[x.id] = UserSubmission.objects.filter(game=x.id).count()
        d = dict(reversed(sorted(d.items(), key=lambda i:i[1])))
        #serializer = GameEntrySerializer(gameEntries, many=True)
        return Response(d, status=status.HTTP_200_OK)
    
class GameEntryDataConfigApiView(APIView):
    permission_classes = []

    def get(self, request, gameid, *args, **kwargs):
        gameEntry = GameEntry.objects.filter(id=gameid).first()
        return Response(json.loads(gameEntry.dataConfigJson), status=status.HTTP_200_OK)
    
class UserSubmissionListApiView(APIView):
    permission_classes = []

    def get(self, request, gameid, *args, **kwargs):
        userSubmissions = UserSubmission.objects.filter(game=gameid)
        serializer = UserSubmissionSerializer(userSubmissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserSubmissionFilteredListApiView(APIView):
    permission_classes = []

    def get(self, request, gameid, filterstring: str, *args, **kwargs):
        userSubmissions = UserSubmission.objects
        try:
            for x in filterstring.split(';'):
                y = x.split(':')
                if y[0] == "data1":
                    userSubmissions = userSubmissions.filter(data1__gte=int(y[1].split('~')[0])) if '~' in y[1] else userSubmissions.filter(data1=int(y[1]))
                    userSubmissions = userSubmissions.filter(data1__lte=int(y[1].split('~')[1])) if '~' in y[1] else userSubmissions
                elif y[0] == "data2":
                    userSubmissions = userSubmissions.filter(data2__gte=int(y[1].split('~')[0])) if '~' in y[1] else userSubmissions.filter(data2=int(y[1]))
                    userSubmissions = userSubmissions.filter(data2__lte=int(y[1].split('~')[1])) if '~' in y[1] else userSubmissions
                elif y[0] == "data3":
                    userSubmissions = userSubmissions.filter(data3__gte=int(y[1].split('~')[0])) if '~' in y[1] else userSubmissions.filter(data3=int(y[1]))
                    userSubmissions = userSubmissions.filter(data3__lte=int(y[1].split('~')[1])) if '~' in y[1] else userSubmissions
                elif y[0] == "data4":
                    userSubmissions = userSubmissions.filter(data4__gte=int(y[1].split('~')[0])) if '~' in y[1] else userSubmissions.filter(data4=int(y[1]))
                    userSubmissions = userSubmissions.filter(data4__lte=int(y[1].split('~')[1])) if '~' in y[1] else userSubmissions
                elif y[0] == "name":
                    userSubmissions = userSubmissions.filter(playername__icontains=y[1])
            serializer = UserSubmissionSerializer(userSubmissions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Invalid filter string'}, status=status.HTTP_400_BAD_REQUEST)
    
#
#   USER
#

class UserSubmissionUserListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, gameid, *args, **kwargs):
        jsonGameData = GameEntry.objects.filter(id=gameid).first().dataConfigJson
        jsonStr = "{\"required_fields\": [\"playername\", \"playerurl\", \"data1\", \"data2\", \"data3\", \"data4\"], \"jsonConf\": "+jsonGameData+"}"
        return Response(json.loads(jsonStr), status=status.HTTP_200_OK)

    def post(self, request, gameid, *args, **kwargs):
        newSubmission = {
            'user': request.user.id,
            'game': gameid,
            'playername': request.data.get('playername'),
            'playerurl': request.data.get('playerurl'),
            'data1': request.data.get('data1'),
            'data2': request.data.get('data2'),
            'data3': request.data.get('data3'),
            'data4': request.data.get('data4'),
            'submissiondate': datetime.datetime.now()
        }
        for x in range(1,5):
            if newSubmission[f'data{x}'] is None:
                newSubmission[f'data{x}'] = 0
        serializer = UserSubmissionSerializer(data=newSubmission)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserOwnSubmissionsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        userSubmissions = UserSubmission.objects.filter(user=request.user.id)
        serializer = UserSubmissionSerializer(userSubmissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#
#   ADMIN
#

class GameEntryAdminListApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        gameEntries = GameEntry.objects.all()
        serializer = GameEntrySerializer(gameEntries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        newGameEntry = {
            'name': request.data.get('name'),
            'dataConfigJson': request.data.get('dataConfigJson')
        }
        serializer = GameEntrySerializer(data=newGameEntry)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class GameEntryDetailsAdminListApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, gameid, *args, **kwargs):
        gameEntry = GameEntry.objects.get(id=gameid)
        serializer = GameEntrySerializer(gameEntry, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, gameid, *args, **kwargs):
        gameEntry = GameEntry.objects.get(id=gameid)
        newGameEntry = {
            'name': request.data.get('name'),
            'dataConfigJson': request.data.get('dataConfigJson')
        }
        serializer = GameEntrySerializer(instance=gameEntry, data=newGameEntry, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, gameid, *args, **kwargs):
        target = GameEntry.objects.get(id=gameid)
        target.delete()
        return Response(status=status.HTTP_200_OK)
