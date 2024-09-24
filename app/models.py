from django.db import models

# Create your models here.

class BasicQuestion(models.Model):
    age = models.TextField()
    gender = models.TextField()
    
    