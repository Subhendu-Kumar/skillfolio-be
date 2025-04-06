from django.urls import path
from user_profile.views import (
    UserProfileDetailView,
    UserProfileUpdateView,
)

urlpatterns = [
    path("detail/", UserProfileDetailView.as_view(), name="profile-detail"),
    path("update/", UserProfileUpdateView.as_view(), name="profile-update"),
]
