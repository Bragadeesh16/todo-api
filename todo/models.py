from django.db import models

# Create your models here.

class todo_model(models.Model):
    todo = models.CharField(max_length=100)