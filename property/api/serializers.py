from rest_framework import serializers
from proprietary.models import Owner
from property import models
from django.contrib.auth.models import User

class TypeSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=70)

	class Meta:
		model = models.Type
		fields= ['id','name']
	
	def exist(self, validate_data):
		try:
		 	valor= models.Type.objects.get(name=validate_data['name'])
		 	return True
		except models.Type.DoesNotExist:
		 	return False

	def create(self, validate_data):
		if self.exist(validate_data)==False:
			return models.Type.objects.create(**validate_data)
		return None

	def update_final(self, instance, validate_data):
		instance.name = validate_data.get('name',instance.name)
		instance.save()

	def save(self):
		if self.create(self.data) is None:
			self._errors = {'name':['alread exist']}
			return False
		return True

	def update(self, instance):
		self.update_final(instance,self.data)


class PatrimonySerializer(serializers.ModelSerializer):
	owner = serializers.UUIDField()
	type = serializers.CharField(max_length=70)
	name = serializers.CharField(max_length=100)
	description = serializers.CharField()
	file = serializers.FileField(allow_null=True)

	class Meta:
		model = models.Patrimony
		fields= ['id','name','type','owner','file','description','created','images']

	def create(self, validate_data):
		validate_data['type_id']= self.tratar_type(validate_data,None)
		del validate_data['type']
		
		validate_data['owner_id'] = self.tratar_owner(validate_data,None)
		del validate_data['owner']

		if validate_data['owner_id'] is None:
			return None
		return models.Patrimony.objects.create(**validate_data)

	def tratar_type(self, validate_data,type_id):
		type = validate_data['type']
		if type!="":
			try:
				return models.Type.objects.get(name=type)
			except models.Type.DoesNotExist:
				pass
		return type_id

	def tratar_owner(self, validate_data,owner_id):
		owner = validate_data['owner']
		if owner!="":
			try:
				return Owner.objects.get(pk=owner)
			except Owner.DoesNotExist:
				pass
		return owner_id

	def update_final(self, instance, validate_data):
		instance.type_id =self.tratar_type(validate_data,instance.type_id)
		instance.name = validate_data.get('name',instance.name)
		instance.owner_id = self.tratar_owner(validate_data,instance.owner_id)
		instance.description = validate_data.get('description',instance.description)
		instance.file = validate_data.get('file',instance.file)
		instance.save()

	def save(self):
		if self.create(self.data) is None:
			self._errors = {'owner':['not found']}
			return False
		return True

	def update(self, instance):
		self.update_final(instance,self.data)


class ImageSerializer(serializers.ModelSerializer):
	image = serializers.ImageField()
	patrimony_id = serializers.UUIDField()

	class Meta:
		model = models.Image
		fields= ['id','image','patrimony_id']
	
	def exist_patrimony(self, validate_data, patrimony_id):
		patrimony = validate_data['patrimony_id']
		if patrimony!="":
			try:
				return models.Patrimony.objects.get(pk=patrimony)
			except models.Patrimony.DoesNotExist:
				pass
		return patrimony_id

	def create(self, validate_data):
		validate_data['patrimony_id']=self.exist_patrimony(validate_data,None)
		if validate_data['patrimony_id'] is None:
			return None
		return models.Image.objects.create(**validate_data)

	def update_final(self, instance, validate_data):
		instance.image = validate_data.get('image',instance.image)
		instance.save()

	def save(self):
		if self.create(self.data) is None:
			self._errors = {'patrimony_id':['not found']}
			return False
		return True

	def update(self, instance):
		self.update_final(instance,self.data)