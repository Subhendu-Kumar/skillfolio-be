from rest_framework import serializers  # type: ignore
from stats.models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ["id", "user", "jobs_visited"]
        read_only_fields = ["id", "user", "jobs_visited"]
