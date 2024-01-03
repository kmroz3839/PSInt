from django.urls import path, include

from rest_framework import routers

from .views import (
    TeamsListAPIView,
    AdminTeamsView,
    UserInTeamsListAPIView,
    UserRemoveFromTeamAPIView,
    UserCreateTeamAPIView,
    UserJoinTeamAPIView,
    AdminUsersInTeamsView
)

router = routers.DefaultRouter()
router.register('admin/teams', AdminTeamsView)
router.register('admin/usersinteams', AdminUsersInTeamsView)

urlpatterns = [
    path('public/teams/', TeamsListAPIView.as_view()),
    path('user/profile/teams/', UserInTeamsListAPIView.as_view()),
    path('user/profile/teams/join/', UserJoinTeamAPIView.as_view()),
    path('user/profile/teams/leave/<int:targetteam>/', UserRemoveFromTeamAPIView.as_view()),
    path('user/profile/teams/create', UserCreateTeamAPIView.as_view()),
]

urlpatterns += router.urls