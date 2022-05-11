from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework import status

def ok(id=None):
	if id is None:
		return {'status':'ok'}
	return {'status':'ok','id':id}

def not_found():
	return {'status':'not found'}

##################################################################
class List(APIView):
	serializer_class = None
	queryset = None

	def get(self, request):
		serializer = self.serializer_class(self.queryset.all(),many=True)
		return JsonResponse(serializer.data, safe=False,status=status.HTTP_200_OK)

class Create(APIView):
	serializer_class = None

	def post(self,request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(ok(), status=status.HTTP_201_CREATED)
		return JsonResponse(serializer.errors,safe=False,status=status.HTTP_400_BAD_REQUEST)

class ListCreateAPIView(List,Create):
	pass
	

#######################################################################
class Detail(APIView):
	serializer_class = None
	model_class = None

	def get_object(self, pk):
		try:
			return  self.model_class.objects.get(pk=pk)
		except self.model_class.DoesNotExist:
			return None
			#JsonResponse(not_found(),status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		object = self.get_object(pk)
		if object is None: 
			return JsonResponse(not_found(),safe=False,status=status.HTTP_404_NOT_FOUND)
		serializer = self.serializer_class(object)
		return JsonResponse(serializer.data,safe=False)


class Alter(APIView):
	serializer_class = None
	model_class = None

	def get_object(self, pk):
		try:
			return  self.model_class.objects.get(pk=pk)
		except self.model_class.DoesNotExist:
			return None
			#JsonResponse(not_found(),status=status.HTTP_404_NOT_FOUND)

	def put(self,request, pk):
		object= self.get_object(pk)
		if object is None:
			return JsonResponse(not_found(),safe=False,status=status.HTTP_404_NOT_FOUND)
		serializer = self.serializer_class(object,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(ok(),safe=False,status=status.HTTP_200_OK)
		return JsonResponse(serializer.errors,safe=False,status=status.HTTP_400_BAD_REQUEST)


class Delete(APIView):
	model_class = None

	def get_object(self, pk):
		try:
			return  self.model_class.objects.get(pk=pk)
		except self.model_class.DoesNotExist:
			return None
			#JsonResponse(not_found(),status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, pk):
		object = self.get_object(pk)
		if object is None:
			return JsonResponse(not_found(),safe=False,status=status.HTTP_404_NOT_FOUND)
		object.delete()
		return JsonResponse(ok(),safe=False,status=status.HTTP_204_NO_CONTENT)


class DetailPutDeleteAPIView(Detail,Alter,Delete):
	pass