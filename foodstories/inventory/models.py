from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
    ("Male", ("Male")),
    ("Female", ("Female"))
)
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = models.ImageField(upload_to='images')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    text = models.TextField(max_length=3000)
    picture = models.ImageField(upload_to='images')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='recipe')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, db_index=True, related_name='recipe')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

class Comments(models.Model):
    recipes = models.ForeignKey('Recipe', on_delete=models.CASCADE, db_index=True, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='comments')
    text = models.TextField(max_length=1000)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Category(models.Model):
    tagname = models.CharField(max_length=80)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tagname}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    