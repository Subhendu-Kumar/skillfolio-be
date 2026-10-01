from stats.models import Statistics
from rest_framework import serializers


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = "__all__"
