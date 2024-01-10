from django.urls import path, include
from rest_framework import routers

from tf_team import urls as tf_team_urls
from tf_auth import urls as tf_auth_urls

from .views import (
    AdminGameEntryViewSet,
    AdminUserReportsViewSet,

    GameEntryListApiView, 
    GameEntryRankingListApiView, 
    UserSubmissionUserListApiView, 
    UserOwnSubmissionsApiView, 
    UserSubmissionFilteredListApiView, 
    UserReportPlayerApiView, 
    GameEntryDetailsAdminListApiView, 
    GameEntryDataConfigApiView, 
    GameSuggestionsListAdminApiView,
    TFUserApiView,
    UserSubmissionListApiView,
    UserSuggestGameApiView,
)

router = routers.DefaultRouter()
router.register('admin/games', AdminGameEntryViewSet)
router.register('admin/reports', AdminUserReportsViewSet)

urlpatterns = [
    path('public/games/', GameEntryListApiView.as_view()),
    path('public/games/<int:gameid>/submissions/', UserSubmissionListApiView.as_view()),
    path('public/games/<int:gameid>/submissions/<str:filterstring>/', UserSubmissionFilteredListApiView.as_view()),
    path('public/games/<int:gameid>/dataconfig/', GameEntryDataConfigApiView.as_view()),
    path('public/gamesranking/', GameEntryRankingListApiView.as_view()),
    path('public/user/<int:uid>/', TFUserApiView.as_view()),
    path('user/profile/submissions', UserOwnSubmissionsApiView.as_view()),
    path('user/submit/<int:gameid>/', UserSubmissionUserListApiView.as_view()),
    path('user/report/', UserReportPlayerApiView.as_view()),
    path('user/suggestgame/', UserSuggestGameApiView.as_view()),
    path('admin/games/<int:gameid>/', GameEntryDetailsAdminListApiView.as_view()),
    path('admin/suggestions/', GameSuggestionsListAdminApiView.as_view()),

    path('', include(tf_team_urls)),
    path('auth/', include(tf_auth_urls)),
]

urlpatterns += router.urls