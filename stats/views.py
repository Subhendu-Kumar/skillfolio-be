from stats.models import Statistics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from stats.serializers import StatisticsSerializer


class StatisticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        stats = get_object_or_404(Statistics, user=request.user)
        serializer = StatisticsSerializer(stats)
        return Response(serializer.data)

    def post(self, request):
        stats, _ = Statistics.objects.get_or_create(user=request.user)
        serializer = StatisticsSerializer(
            instance=stats, data=request.data, partial=True
        )
        if serializer.is_valid():
            stats.jobs_visited += 1
            stats.save()
            return Response(StatisticsSerializer(stats).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
