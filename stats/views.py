# views.py
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status, permissions  # type: ignore
from stats.models import Statistics
from stats.serializers import StatisticsSerializer


class StatisticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        stats, _ = Statistics.objects.get_or_create(
            user=request.user, defaults={"jobs_visited": 0}
        )
        serializer = StatisticsSerializer(stats)
        return Response(serializer.data)

    def post(self, request):
        stats, created = Statistics.objects.get_or_create(
            user=request.user, defaults={"jobs_visited": 0}
        )
        stats.jobs_visited += 1
        stats.save()
        serializer = StatisticsSerializer(stats)
        return Response(serializer.data, status=status.HTTP_200_OK)
