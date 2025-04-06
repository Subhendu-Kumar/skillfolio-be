from django.urls import path
from jobs.views import get_latest_jobs, get_job_details

urlpatterns = [
    path("latest/jobs/", get_latest_jobs.as_view(), name="latest-jobs"),
    path("job/details/<str:job_id>", get_job_details.as_view(), name="job-details"),
]
