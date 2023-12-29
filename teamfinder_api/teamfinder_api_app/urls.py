from django.urls import path, include

from .views import GameEntryListApiView, GameEntryAdminListApiView, UserSubmissionUserListApiView, GameEntryDetailsAdminListApiView, GameEntryDataConfigApiView, UserSubmissionListApiView

urlpatterns = [
    path('public/games/', GameEntryListApiView.as_view()),
    path('public/games/<int:gameid>/submissions/', UserSubmissionListApiView.as_view()),
    path('public/games/<int:gameid>/dataconfig/', GameEntryDataConfigApiView.as_view()),
    path('user/submit/<int:gameid>/', UserSubmissionUserListApiView.as_view()),
    path('admin/games/', GameEntryAdminListApiView.as_view()),
    path('admin/games/<int:gameid>/', GameEntryDetailsAdminListApiView.as_view()),
]