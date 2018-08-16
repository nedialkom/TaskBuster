# -*- coding: utf-8 -*-

# Register your models here.
from django.contrib import admin
from . import models
 
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("username", "interaction")

    search_fields = ["user__username"]
