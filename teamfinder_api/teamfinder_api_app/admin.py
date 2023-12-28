from django.contrib import admin

from .models import GameEntry, UserSubmission

# Register your models here.

admin.site.register(GameEntry)
admin.site.register(UserSubmission)