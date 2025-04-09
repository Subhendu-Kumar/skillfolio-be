from google import genai
from django.conf import settings
from resume_ats.prompts import master_prompt_ats, master_prompt_enhance_resume

client = genai.Client(api_key=settings.GEMINI_API_KEY)
model = "gemini-2.0-flash"


def get_ats_score_with_vision(images_base64, job_description):
    contents = [
        {"text": master_prompt_ats},
        {"text": f"Job Description:\n{job_description}"},
    ]

    for img in images_base64:
        contents.append({"inline_data": img})

    response = client.models.generate_content(
        model=model,
        contents=contents,
    )

    return response.text


def get_enhanced_resume(images_base64, job_description):
    contents = [
        {"text": master_prompt_enhance_resume},
        {"text": f"Job Description:\n{job_description}"},
    ]

    for img in images_base64:
        contents.append({"inline_data": img})

    response = client.models.generate_content(
        model=model,
        contents=contents,
    )

    return response.text
