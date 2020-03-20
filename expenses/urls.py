from django.urls import path

from .views import SpentView

urlpatterns = [
    path('spent/', SpentView.as_view(), name='spent'),
]