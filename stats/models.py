import uuid
from django.db import models
from django.conf import settings


class Statistics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="statistics"
    )

    jobs_visited = models.IntegerField(default=0)

    class Meta:
        db_table = "statistics"
        verbose_name = "statistics"
        verbose_name_plural = "statistics"
