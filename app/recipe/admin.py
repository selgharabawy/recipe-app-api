"""
Django admin customization for Recipe APP
"""
from django.contrib import admin
from recipe import models


admin.site.register(models.Recipe)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
