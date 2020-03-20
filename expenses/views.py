from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Spent
from .serializers import SpentSerializer

# Create your views here.

class SpentView(generics.ListCreateAPIView):
    queryset = Spent.objects.all()
    serializer_class = SpentSerializer