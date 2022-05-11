from django.shortcuts import render
from Property_Management import super_apiviews
from property.api import serializers
from property import models
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


###############TYPE##########################
class TypeList(super_apiviews.ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class = serializers.TypeSerializer
	queryset = models.Type.objects.all()

class TypeDetail(super_apiviews.DetailPutDeleteAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = serializers.TypeSerializer
	model_class = models.Type

############Patrimony#########################
class PatrimonyList(super_apiviews.ListCreateAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = serializers.PatrimonySerializer
	queryset = models.Patrimony.objects.all()

class PatrimonyDetail(super_apiviews.DetailPutDeleteAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = serializers.PatrimonySerializer
	model_class = models.Patrimony

########Image###############################
class ImageList(super_apiviews.ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class = serializers.ImageSerializer
	queryset = models.Image.objects.all()

class ImageDetail(super_apiviews.DetailPutDeleteAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class = serializers.ImageSerializer
	model_class = models.Image