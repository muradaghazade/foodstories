from django.contrib import admin
from inventory.models import Recipe, Author, Comments, Reply

# Register your models here.
admin.site.register([Recipe, Author, Comments, Reply])