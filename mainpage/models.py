from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.urls import reverse

class Profile(models.Model):
    birthday = models.DateField(null=True, blank=True)
    about = models.TextField(max_length=1000, help_text='Немного о себе')
    user = models.OneToOneField(User, on_delete=CASCADE, null=True)
    



