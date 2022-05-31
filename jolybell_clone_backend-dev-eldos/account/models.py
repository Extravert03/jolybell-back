from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=64, blank=True)
    region = models.CharField(max_length=64, blank=True)
    post_code = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64, blank=True)
    address = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f'{self.user} profile'
