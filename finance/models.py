from django.db import models
from django.urls import reverse
from property.models import Patrimony
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Valuetion(models.Model):
	id = models.UUIDField(primary_key=True, default= uuid.uuid4)
	user_id = models.ForeignKey(User, verbose_name='User',on_delete=models.CASCADE)
	patrimony_id = models.ForeignKey(Patrimony,verbose_name='Patrimony',on_delete=models.CASCADE)
	value = models.FloatField()
	description  = models.TextField()

	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-update']

	def __str__(self):
		return str(self.value)

	def user(self):
		return self.user_id.__str__()

	def get_absolute_url(self):
		return reverse("valuetion_detail",kwargs={"pk":self.id})