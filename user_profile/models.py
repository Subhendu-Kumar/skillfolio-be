import uuid
from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )

    # Basic Info
    full_name = models.CharField(max_length=255, blank=True, default="demo name")
    phone_number = models.CharField(max_length=20, blank=True, default="1230987654")
    location = models.CharField(max_length=255, blank=True, default="india")
    bio = models.TextField(blank=True, default="demo demo")

    # Education
    highest_qualification = models.CharField(
        max_length=255, blank=True, default="example"
    )
    university = models.CharField(max_length=255, blank=True, default="example")
    graduation_year = models.PositiveIntegerField(blank=True, default=2004)

    # Experience
    current_position = models.CharField(max_length=255, blank=True, default="example")
    experience_years = models.DecimalField(
        max_digits=4, decimal_places=1, blank=True, default=4.5
    )

    # Skills
    skills = models.TextField(
        blank=True,
        default="example, demo",
        help_text="Comma-separated skills (e.g. Python, Django, React)",
    )

    # Socials
    linkedin = models.URLField(blank=True, default="https://example.com")
    github = models.URLField(blank=True, default="https://example.com")
    portfolio = models.URLField(blank=True, default="https://example.com")

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
