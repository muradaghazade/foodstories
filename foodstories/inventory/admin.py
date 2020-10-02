from django.contrib import admin
from inventory.models import Recipe, Comments

# Register your models here.
admin.site.register([Recipe, Comments])