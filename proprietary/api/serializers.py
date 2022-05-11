from rest_framework import serializers
from proprietary import models
from django.contrib.auth.models import User

class OwnerSerializer(serializers.ModelSerializer):
	user = serializers.CharField(allow_blank=True)
	first_name = serializers.CharField(max_length=64)
	last_name = serializers.CharField(max_length=64,allow_blank=True)

	class Meta:
		model = models.Owner
		fields= ['id','user','first_name','last_name','created']

	def create(self, validate_data):
		validate_data['user_id'] = self.tratar_user_id(validate_data,None)
		del validate_data['user']
		return models.Owner.objects.create(**validate_data)

	def tratar_user_id(self, validate_data, user_id):
		user = validate_data['user']
		if user!="":
			try:
				return User.objects.get(username=user)
			except User.DoesNotExist:
				pass
		return user_id

	def update_final(self, instance, validate_data):
		instance.user_id =self.tratar_user_id(validate_data,instance.user_id)
		instance.first_name = validate_data.get('first_name',instance.first_name)
		instance.last_name = validate_data.get('last_name',instance.last_name)
		instance.save()

	def save(self):
		if self.create(self.data) is None:
			self._errors = {'user':['not found']}
			return False
		return True

	def update(self, instance):
		self.update_final(instance,self.data)