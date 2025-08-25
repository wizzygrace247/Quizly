from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    score = models.IntegerField(default=0)

    def __str__(self):
       return self.user.uername


