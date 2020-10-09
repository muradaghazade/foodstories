from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (
    ("Male", ("Male")),
    ("Female", ("Female"))
)
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = models.ImageField(upload_to='images')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    email = models.EmailField(('email adress'), unique=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'