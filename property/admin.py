from django.contrib import admin
from property.models import Type, Patrimony, Image
# Register your models here.

class ImageInline(admin.TabularInline):
	model=Image
	extra=0
	can_delete=True

class TypeAdmin(admin.ModelAdmin):
	list_display = ('id','name','created')
	list_filter = ('created','update')
	fields=['name']
	search_fields = ['name']
admin.site.register(Type,TypeAdmin)

class PatrimonyAdmin(admin.ModelAdmin):
	list_display = ('id','name','owner_id','created')
	list_filter = ('type_id','created','update')
	inlines=[ImageInline]
	fieldsets = (
			(None,{'fields':('type_id','owner_id')}),
			('Detail',{'fields':('name','file','description')})
		)
	search_fields = ['name']
admin.site.register(Patrimony,PatrimonyAdmin)