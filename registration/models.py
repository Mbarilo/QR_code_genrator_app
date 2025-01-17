from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length= 50)
    password = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    def __str__(self):
        return self.name