from django.urls import path

from .views import SpentView, StatisticsMonthlyView

urlpatterns = [
    path('spent/', SpentView.as_view(), name='spent'),
    path('statistics/<int:month>', StatisticsMonthlyView.as_view(), name='monthly-statistics'),
]