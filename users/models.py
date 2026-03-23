from django.contrib.auth.models import AbstractUser
from django.db import models
from .custom_user_manager import CustomUserManager
from django.conf import settings

class CustomUser(AbstractUser):
    username = None  
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=[('admin', 'Administrator'), ('visitor', 'Visitor')],
        default='visitor',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)