from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QrCodes(models.Model):
    name = models.CharField(max_length= 20, unique= True)
    image = models.TextField(default= "none")
    user = models.ForeignKey(User, models.CASCADE)
