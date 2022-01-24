from django.contrib.auth.models import User
from django.db import models


class MailChimpToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=500)
    server = models.CharField(max_length=25)