from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.db.models import Q
from django.db.models import Sum

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


class StatisticsMonthlyView(APIView):
    def get(self, request, month):
        salary_qs = Spent.objects.filter(
            Q(type='salary') & Q(time__month=month))
        meals_qs = Spent.objects.filter(
            Q(type='company_meals') & Q(time__month=month))
        snacks_qs = Spent.objects.filter(
            Q(type='company_snacks') & Q(time__month=month))
        electronics_qs = Spent.objects.filter(
            Q(type='electronics') & Q(time__month=month))
        sponsor_qs = Spent.objects.filter(
            Q(type='sponsor') & Q(time__month=month))
        etc_qs = Spent.objects.filter(
            Q(type='etc') & Q(time__month=month))
        
        monthly_total = [{
            'monthly_total_price': Spent.objects.filter(time__month=month).aggregate(Sum('price')),
            'total_salary': salary_qs.aggregate(Sum('price')),
            'total_meals': meals_qs.aggregate(Sum('price')),
            'total_snacks': snacks_qs.aggregate(Sum('price')),
            'total_electronics': electronics_qs.aggregate(Sum('price')),
            'total_sponsor': sponsor_qs.aggregate(Sum('price')),
            'total_etc': etc_qs.aggregate(Sum('price')),
            }]

        return JsonResponse(monthly_total, safe=False)





