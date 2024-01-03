from django.contrib import admin

from .models import GameEntry, UserSubmission, UserReport, GameSuggestion

# Register your models here.

admin.site.register(GameEntry)
admin.site.register(UserSubmission)
admin.site.register(UserReport)
admin.site.register(GameSuggestion)