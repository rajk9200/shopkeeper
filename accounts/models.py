from django.db import models

# Create your models here.

class Accounts(models.Model):
    username =models.CharField(max_length=100, unique=True)
    email =models.EmailField(unique=True)
    password =models.CharField(max_length=100)
    mobile =models.CharField(max_length=12)

    def __str__(self):
        return self.username