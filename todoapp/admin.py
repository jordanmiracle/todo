from django.contrib import admin
from .models import Todo
from datetime import datetime


# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('title', 'memo', 'completed')


admin.site.register(Todo, TodoAdmin)
