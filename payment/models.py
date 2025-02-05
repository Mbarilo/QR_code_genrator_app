from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class RandomCodes(models.Model):
    random_code = models.CharField(max_length= 6)
    user = models.OneToOneField(to= User, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.random_code