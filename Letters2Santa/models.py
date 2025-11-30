from django.db import models
from django.contrib.auth.models import User

class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    letter = models.TextField()
    wishlist = models.TextField(blank=True)
    response = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)