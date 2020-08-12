from django.contrib import admin
from .models import Type, Task, Status


class TaskAdmin(admin.ModelAdmin):
    list_display = ('summary', 'status', 'created_at')
    fields = ['summary', 'description', 'status', 'type']
    search_fields = ('summary',)
    list_filter = ('status',)


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
