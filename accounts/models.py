from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=150, null=True)
    lastname = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, null=True)