from django.db import models

class Settings(models.Model):
    title = models.CharField(max_length=50)
    key = models.CharField(max_length=100)
    value =models.CharField(max_length=100)
    Editable = models.BooleanField()
    type = models.CharField(max_length=50)