from django.db import models

# Create your models here.

class BasicQuestion(models.Model):
    age = models.TextField()
    gender = models.TextField()
    awareness1 = models.TextField()
    awareness2 = models.TextField()
    awareness3 = models.TextField()
    financial1 = models.TextField()
    financial2 = models.TextField()