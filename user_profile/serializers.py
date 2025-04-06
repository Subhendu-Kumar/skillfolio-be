from rest_framework import serializers  # type: ignore
from user_profile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ["id", "user", "created_at"]
