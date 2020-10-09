from django.contrib import admin
from inventory.models import Recipe, Comments, Category, ContactUs

# Register your models here.
admin.site.register([Recipe, Comments, Category, ContactUs])