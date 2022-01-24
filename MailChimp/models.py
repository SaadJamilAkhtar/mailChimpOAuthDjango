from django.contrib.auth.models import User
from django.db import models


class MailChimpToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=500)
    server = models.CharField(max_length=25)


class MailChimpCredentials(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    callback = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Mail Chimp Credentials"
