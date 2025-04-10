# views.py
from stats.models import Statistics
from stats.serializers import StatisticsSerializer
from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status, permissions  # type: ignore


class StatisticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        stats = Statistics.objects.get(
            user=request.user,
        )
        serializer = StatisticsSerializer(stats)
        return Response(serializer.data)

    def post(self, request):
        stats, create = Statistics.objects.get_or_create(user=request.user)
        stats.jobs_visited += 1
        stats.save()
        serializer = StatisticsSerializer(stats)
        return Response(serializer.data, status=status.HTTP_200_OK)
