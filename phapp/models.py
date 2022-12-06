from django.db import models

# Create your models here.

class phonebookt(models.Model):
    name=models.CharField(max_length=30)
    num=models.CharField(max_length=30)