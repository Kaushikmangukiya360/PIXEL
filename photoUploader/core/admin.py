from django.contrib import admin

from .models import imgData

# Register your models here.
# admin.site.register(imgData)

@admin.register(imgData)
class imgDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'img', 'dateandtime']