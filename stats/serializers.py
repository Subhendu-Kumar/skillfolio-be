from rest_framework import serializers  # type: ignore
from stats.models import Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = "__all__"
