import requests  # type: ignore
from django.conf import settings
from rest_framework import status  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore

headers = {
    "X-Rapidapi-Key": settings.RAPID_API_KEY,
    "X-Rapidapi-Host": settings.RAPID_API_HOST,
}


class get_latest_jobs(APIView):
    def get(self, request):
        query = request.query_params.get("query", "latest software jobs")
        url = (
            f"https://{settings.RAPID_API_HOST}/search"
            f"?query={query}&num_pages=1&country=IN&sort_by=latest_job_posted"
        )

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.HTTPError as errh:
            return Response({"error": str(errh)}, status=response.status_code)
        except requests.exceptions.RequestException as err:
            return Response(
                {"error": "Failed to connect to Jsearch api."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        simplified_jobs = [
            {
                "job_id": job.get("job_id"),
                "job_title": job.get("job_title"),
                "employer_name": job.get("employer_name"),
                "job_posted_at": job.get("job_posted_at"),
            }
            for job in data.get("data", [])
        ]
        res = {
            "success": True,
            "message": "jobs retrived successfully",
            "jobs": simplified_jobs,
        }

        return Response(res, status=status.HTTP_200_OK)


class get_job_details(APIView):
    def get(self, request, job_id):
        url = f"https://{settings.RAPID_API_HOST}/job-details?job_id={job_id}"

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.HTTPError as errh:
            return Response({"error": str(errh)}, status=response.status_code)
        except requests.exceptions.RequestException as err:
            return Response(
                {"error": "Failed to connect to Jsearch api."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        if data.get("data"):
            job = data["data"][0]
            filtered_job = {
                "job_id": job.get("job_id"),
                "job_title": job.get("job_title"),
                "employer_name": job.get("employer_name"),
                "employer_logo": job.get("employer_logo"),
                "employer_website": job.get("employer_website"),
                "job_publisher": job.get("job_publisher"),
                "job_employment_type": job.get("job_employment_type"),
                "job_apply_link": job.get("job_apply_link"),
                "job_description": job.get("job_description"),
                "job_posted_at": job.get("job_posted_at"),
                "job_posted_at_datetime_utc": job.get("job_posted_at_datetime_utc"),
                "job_location": job.get("job_location"),
            }
            res = {
                "success": True,
                "message": "Successfully get the job details",
                "details": filtered_job,
            }
            return Response(res, status=status.HTTP_200_OK)

        return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
