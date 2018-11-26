from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100, null=False, primary_key=True)
    public_name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
    institution = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.email