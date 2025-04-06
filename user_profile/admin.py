from django.contrib import admin
from user_profile.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "location", "created_at")
    search_fields = ("user__email", "full_name", "location")
