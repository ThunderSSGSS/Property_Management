from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Owner(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	user_id = models.ForeignKey(User, verbose_name='User',null=True,blank=True,on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64,blank=True)

	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-update']

	def __str__(self):
		if self.last_name=="":
			return self.first_name
		return self.first_name+" "+self.last_name

	def user(self):
		if self.user_id is None:
			return ""
		return self.user_id.__str__()
		

	def get_absolute_url(self):
		return reverse("owner_detail",kwargs={"pk":self.id})