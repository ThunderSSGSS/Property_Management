from django.db import models
from proprietary.models import Owner
from django.urls import reverse
import uuid
# Create your models here.

def patrimony_image_dir():
	return 'static/media/patrimony/image'

def patrimony_file_dir():
	return 'static/media/patrimony/file'

class Type(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=70)

	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering=['name']

	def get_absolute_url(self):
		return reverse("type_detail",kwargs={"pk":self.id})

	def __str__(self):
		return self.name

class Patrimony(models.Model):
	id = models.UUIDField(primary_key=True, default= uuid.uuid4)
	type_id = models.ForeignKey(Type,null=True,on_delete=models.SET_NULL)
	owner_id  = models.ForeignKey(Owner, verbose_name='Proprietary',on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	file = models.FileField(null=True,blank=True,upload_to=patrimony_file_dir())
	description = models.TextField()

	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural='Patrimonies'
		ordering=['-update']

	def owner(self):
		if self.owner_id is None:
			return None
		return self.owner_id.__str__()

	def type(self):
		if self.type_id is None:
			return None
		return self.type_id.__str__()
	
	def images(self):
		queryset = Image.objects.filter(patrimony_id__exact=self.id)
		lista=[]
		for image in queryset:
			lista.append('/'+image.image.__str__())
		return lista

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("patrimony_detail",kwargs={"pk":self.id})

class Image(models.Model):
	id = models.UUIDField(primary_key=True, default= uuid.uuid4)
	patrimony_id = models.ForeignKey(Patrimony,on_delete=models.CASCADE)
	image = models.ImageField(upload_to=patrimony_image_dir())

	def get_absolute_url(self):
		return reverse("patrimony_detail",kwargs={"pk":self.id})