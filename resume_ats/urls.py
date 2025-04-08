from django.urls import path

from resume_ats.views import ResumeImageUploadAPIView

urlpatterns = [
    path("ats/resume/", ResumeImageUploadAPIView.as_view(), name="register"),
]
