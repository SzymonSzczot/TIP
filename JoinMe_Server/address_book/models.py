from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=30)

