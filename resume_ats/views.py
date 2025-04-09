import re, json
from django.http import HttpResponse
from xhtml2pdf import pisa  # type: ignore
from django.template.loader import get_template
from resume_ats.pdfutil import pdf_to_base64_images
from rest_framework import permissions  # type: ignore
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework.parsers import MultiPartParser  # type: ignore
from resume_ats.geminiutil import get_ats_score_with_vision, get_enhanced_resume


class ResumeATSEvaluation(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        resume_file = request.FILES.get("resume")
        job_description = request.data.get("job_description")

        if not resume_file or not job_description:
            return Response(
                {"error": "Resume and job description required."}, status=400
            )

        try:
            images_base64 = pdf_to_base64_images(resume_file)
            ats_result = get_ats_score_with_vision(images_base64, job_description)
            match = re.search(r"```json\n(.*?)```", ats_result, re.DOTALL)
            if not match:
                return Response(
                    {"error": "No valid JSON block found in the response."}, status=422
                )

            json_string = match.group(1)

            try:
                parsed = json.loads(json_string)
            except json.JSONDecodeError as e:
                return Response({"error": f"JSON decode error: {str(e)}"}, status=422)

            return Response({"score_response": parsed})
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class ResumeEnhancer(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        resume_file = request.FILES.get("resume")
        job_description = request.data.get("job_description")

        if not resume_file or not job_description:
            return Response(
                {"error": "Resume and job description required."}, status=400
            )

        try:
            images_base64 = pdf_to_base64_images(resume_file)
            enhance_resume = get_enhanced_resume(images_base64, job_description)
            match = re.search(r"```json\n(.*?)```", enhance_resume, re.DOTALL)
            if not match:
                return Response(
                    {"error": "No valid JSON block found in the response."}, status=422
                )

            json_string = match.group(1)
            try:
                parsed = json.loads(json_string)
                template = get_template("resume_template.html")
                html = template.render({"resume": parsed["enhanced_resume"]})
                response = HttpResponse(content_type="application/pdf")
                response["Content-Disposition"] = 'attachment; filename="resume.pdf"'
                pisa_status = pisa.CreatePDF(html, dest=response)
                if pisa_status.err:
                    return Response("PDF generation error", status=500)
                return response
            except json.JSONDecodeError as e:
                return Response({"error": f"JSON decode error: {str(e)}"}, status=422)

        except Exception as e:
            return Response({"error": str(e)}, status=500)
