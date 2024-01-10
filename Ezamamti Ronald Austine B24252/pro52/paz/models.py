from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)