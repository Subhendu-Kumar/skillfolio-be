from django.urls import path

from resume_ats.views import ResumeATSEvaluation, ResumeEnhancer

urlpatterns = [
    path("ats/resume/", ResumeATSEvaluation.as_view(), name="ats"),
    path("enhance/resume/", ResumeEnhancer.as_view(), name="enhance"),
]
