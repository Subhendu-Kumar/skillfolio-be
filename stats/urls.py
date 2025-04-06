from django.urls import path
from stats.views import StatisticsView

urlpatterns = [
    path("user/stats/", StatisticsView.as_view(), name="statistics"),
]
