from user_profile.serializers import UserProfileSerializer
from rest_framework import generics, permissions  # type: ignore


# 🔹 Retrieve Profile (GET)
class UserProfileDetailView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


# 🔹 Update Profile (PUT or PATCH)
class UserProfileUpdateView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile = serializer.save()

        required_fields = [
            profile.full_name,
            profile.phone_number,
            profile.highest_qualification,
        ]
        if all(required_fields):
            profile.is_complete = True
            profile.save()
