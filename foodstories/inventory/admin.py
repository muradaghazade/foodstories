from django.contrib import admin
from inventory.models import Recipe, Comments, User, Category, ContactUs

# Register your models here.
admin.site.register([Recipe, Comments, User, Category, ContactUs])