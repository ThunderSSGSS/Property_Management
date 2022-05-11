from rest_framework import serializers
from finance import models
from django.contrib.auth.models import User
from property.models import Patrimony

class ValuetionSerializer(serializers.ModelSerializer):
	user = serializers.CharField()
	patrimony_id = serializers.UUIDField()
	description = serializers.CharField()
	value = serializers.FloatField()

	class Meta:
		model = models.Valuetion
		fields= ['id','user','patrimony_id','value','description','update','created']

	def create(self, validate_data):
		validate_data['user_id'] = self.tratar_user_id(validate_data,None)
		del validate_data['user']

		if validate_data['user_id'] is None:
			self._errors = {'user':['not found']}
			return None

		validate_data['patrimony_id']=self.tratar_patrimony_id(validate_data,None)
		if validate_data['patrimony_id'] is None:
			self._errors = {'patrimony_id':['not found']}
			return None

		return models.Valuetion.objects.create(**validate_data)

	def tratar_user_id(self, validate_data, user_id):
		user = validate_data['user']
		if user!="":
			try:
				return User.objects.get(username=user)
			except User.DoesNotExist:
				pass
		return user_id

	def tratar_patrimony_id(self, validate_data, patrimony_id):
		patrimony_id2 = validate_data['patrimony_id']
		if patrimony_id2!="":
			try:
				return Patrimony.objects.get(pk=patrimony_id2)
			except Patrimony.DoesNotExist:
				pass
		return patrimony_id

	def update_final(self, instance, validate_data):
		instance.user_id =self.tratar_user_id(validate_data,instance.user_id)
		instance.patrimony_id = self.tratar_patrimony_id(validate_data,instance.patrimony_id)
		instance.description = validate_data.get('description',instance.description)
		instance.value = validate_data.get('value',instance.value)
		instance.save()

	def save(self):
		if self.create(self.data) is None:
			return False
		return True

	def update(self, instance):
		self.update_final(instance,self.data)