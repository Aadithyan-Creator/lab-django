from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=10,)
    DOB = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField(max_length=50)
    
    def __str__(self):
        return self.username