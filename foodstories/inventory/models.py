from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User = get_user_model()

class User(AbstractUser):
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = models.ImageField(upload_to='images')

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField(max_length=3000)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='recipe')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, db_index=True, related_name='recipe')


class Comments(models.Model):
    recipes = models.ForeignKey('Recipe', on_delete=models.CASCADE, db_index=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='comments')
    text = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    tagname = models.CharField(max_length=80)
    