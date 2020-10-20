from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    text = models.TextField(max_length=3000)
    picture = models.ImageField(upload_to='images')
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='recipe')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, db_index=True, related_name='recipe')
    tag = models.ManyToManyField('Tag',  verbose_name=("Tags"))

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

class Tag(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class Category(models.Model):
    tagname = models.CharField(max_length=80)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tagname}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subject} - {self.email}'

    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'

class Subscribe(models.Model):
    email = models.EmailField(max_length=400, unique=True)
    
    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'

    def __str__(self):
        return f'{self.email}'