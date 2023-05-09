from django.contrib import admin
from . import models

@admin.register(models.Client)
class Client(admin.ModelAdmin):
    list_display = ('login',)

@admin.register(models.DomainNameServer)
class Client(admin.ModelAdmin):
    list_display = ('address',)

@admin.register(models.Website)
class Client(admin.ModelAdmin):
    list_display = ('name',)