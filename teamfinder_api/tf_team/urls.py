from django.urls import path, include

from .views import (
    TeamsListAPIView
)

urlpatterns = [
    path('public/teams/', TeamsListAPIView.as_view()),
    #path('public/teams/<int:teamid>/'),
    #path('user/profile/teams/'),
    #path('user/profile/teams/join/'),
    #path('admin/teams/')
]