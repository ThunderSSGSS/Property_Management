from django.contrib import admin
from proprietary.models import Owner
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
# Register your models here

class OwnerAdmin(admin.ModelAdmin):
	list_display = ('id','user_id','first_name','created')
	#list_filter=('created','update')
	fields=['user_id','first_name','last_name']
	search_fields= ['first_name','last_name']
admin.site.register(Owner,OwnerAdmin)