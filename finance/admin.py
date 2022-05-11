from django.contrib import admin
from finance.models import Valuetion
# Register your models here.

class ValuetionAdmin(admin.ModelAdmin):
	list_display = ('id','patrimony_id','value','created')
	list_filter = ('created','update')
	fieldsets = (
			(None,{'fields':('patrimony_id','user_id')}),
			('Detail',{'fields':('value','description')})
		)
admin.site.register(Valuetion,ValuetionAdmin)