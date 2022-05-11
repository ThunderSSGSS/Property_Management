from django.shortcuts import render
from proprietary.api import serializers
from proprietary import models
from Property_Management import super_apiviews
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# Create your views here.


class OwnerList(super_apiviews.ListCreateAPIView):
	permission_classes = [IsAdminUser]
	serializer_class = serializers.OwnerSerializer
	queryset = models.Owner.objects.all()

class OwnerDetail(super_apiviews.DetailPutDeleteAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = serializers.OwnerSerializer
	model_class = models.Owner
