from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdventDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField()