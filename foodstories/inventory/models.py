from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField(max_length=3000)
    added_at = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='recipe')


class Comments(models.Model):
    recipes = models.ForeignKey('Recipe', on_delete=models.CASCADE, db_index=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='comments')
    text = models.TextField(max_length=1000)
    added_at = models.DateTimeField('date published')
