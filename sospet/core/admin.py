from django.contrib import admin
from .models import Pet

# Register your models here.

@admin.register(Pet)
class PerAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'description', 'user']