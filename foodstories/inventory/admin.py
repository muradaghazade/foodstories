from django.contrib import admin
from inventory.models import Recipe, Comments, User

# Register your models here.
admin.site.register([Recipe, Comments, User])