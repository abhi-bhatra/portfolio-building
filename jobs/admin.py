from django.contrib import admin
from .models import Job

@admin.register(Job)
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['image','summary']