import uuid
from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )

    # Basic Info
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Education
    highest_qualification = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)

    # Experience
    current_position = models.CharField(max_length=255, blank=True, null=True)
    experience_years = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, null=True
    )

    # Skills
    skills = models.TextField(
        blank=True, help_text="Comma-separated skills (e.g. Python, Django, React)"
    )

    # Socials
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)

    is_complete = models.BooleanField(
        default=False, help_text="Is the profile complete?"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"

    class Meta:
        db_table = "user_profile"
        verbose_name = "user_profile"
        verbose_name_plural = "user_profiles"
