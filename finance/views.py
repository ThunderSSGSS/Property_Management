from django.shortcuts import render
from finance.api import serializers
from finance import models
from Property_Management import super_apiviews
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.

class ValuetionList(super_apiviews.ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class = serializers.ValuetionSerializer
	queryset = models.Valuetion.objects.all()

class ValuetionDetail(super_apiviews.DetailPutDeleteAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class = serializers.ValuetionSerializer
	model_class = models.Valuetion