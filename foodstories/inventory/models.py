from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField(max_length=3000)
    added_at = models.DateTimeField('date published')
    authors = models.ManyToManyField('Author', db_index=True, related_name='author')

class Author(models.Model):
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE, db_index=True, related_name='author')
    name = models.CharField(max_length=200)
    info = models.TextField(max_length=3000)
    pic = models.ImageField(upload_to='images')

class Comments(models.Model):
    recipes = models.ForeignKey('Recipe', on_delete=models.CASCADE, db_index=True, related_name='comments')
    text = models.TextField(max_length=1000)
    added_at = models.DateTimeField('date published')

class Reply(models.Model):
    comments = models.ForeignKey('Comments', on_delete=models.CASCADE, db_index=True, related_name='reply')
    text = models.TextField(max_length=1000)
    added_at = models.DateTimeField('date published')