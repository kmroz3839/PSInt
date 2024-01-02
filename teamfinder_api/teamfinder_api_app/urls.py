from django.urls import path, include

from .views import (
    GameEntryListApiView, 
    GameEntryRankingListApiView, 
    GameEntryAdminListApiView, 
    UserSubmissionUserListApiView, 
    UserOwnSubmissionsApiView, 
    UserSubmissionFilteredListApiView, 
    UserReportPlayerApiView, 
    GameEntryDetailsAdminListApiView, 
    GameEntryDataConfigApiView, 
    GameSuggestionsListAdminApiView,
    UserSubmissionListApiView,
    UserSuggestGameApiView,
    UserReportsListAdminApiView
)

urlpatterns = [
    path('public/games/', GameEntryListApiView.as_view()),
    path('public/games/<int:gameid>/submissions/', UserSubmissionListApiView.as_view()),
    path('public/games/<int:gameid>/submissions/<str:filterstring>/', UserSubmissionFilteredListApiView.as_view()),
    path('public/games/<int:gameid>/dataconfig/', GameEntryDataConfigApiView.as_view()),
    path('public/gamesranking/', GameEntryRankingListApiView.as_view()),
    path('user/profile/submissions', UserOwnSubmissionsApiView.as_view()),
    path('user/submit/<int:gameid>/', UserSubmissionUserListApiView.as_view()),
    path('user/report/', UserReportPlayerApiView.as_view()),
    path('user/suggestgame/', UserSuggestGameApiView.as_view()),
    path('admin/games/', GameEntryAdminListApiView.as_view()),
    path('admin/games/<int:gameid>/', GameEntryDetailsAdminListApiView.as_view()),
    path('admin/reports/', UserReportsListAdminApiView.as_view()),
    path('admin/suggestions/', GameSuggestionsListAdminApiView.as_view()),
]