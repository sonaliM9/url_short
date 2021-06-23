from django.db import models

# Create your models here.
class Todo(models.Model):
    link = models.CharField(max_length=1000) 
    uid =models.CharField(max_length=10)