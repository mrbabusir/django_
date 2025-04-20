from django.contrib import admin
from .models import Todolist
# Register your models here.
@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_completed')
    list_filter = ('is_completed',)
    search_fields = ('title', 'description')
    list_per_page = 8
    list_editable = ('title', 'is_completed')
    # ordering = ('-id',)
# admin.site.register(Todolist)