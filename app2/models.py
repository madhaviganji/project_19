from django.db import models

# Create your models here.

class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    ccode=models.CharField(max_length=100)