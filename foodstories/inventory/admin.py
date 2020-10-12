from django.contrib import admin
from inventory.models import Recipe, Comments, Category, ContactUs, Tag

# Register your models here.
admin.site.register([Recipe, Comments, Category, ContactUs, Tag])