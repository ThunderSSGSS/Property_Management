from django.contrib import admin
from django.contrib.admin.models import LogEntry
# Register your models here.

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ('user','action_flag','content_type','object_repr')
	list_filter=('action_time','action_flag')
admin.site.register(LogEntry,LogEntryAdmin)
