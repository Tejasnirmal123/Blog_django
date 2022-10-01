from unittest.util import _MAX_LENGTH
from django.db import models



# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.IntegerField(unique=True)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

