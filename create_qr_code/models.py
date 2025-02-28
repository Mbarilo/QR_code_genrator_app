from django.db import models
from django.contrib.auth.models import User
from registration.models import Profile
import datetime


# Create your models here.
class QrCodes(models.Model):
    name = models.CharField(max_length= 20, unique= False)
    image = models.TextField(default= "none")
    user = models.ForeignKey(User, models.CASCADE)
    date = models.DateField(default= datetime.date.today())
    url = models.CharField(max_length= 255, default = "none")
    desktop = models.BooleanField(default= False)

    def __str__(self):
        return self.name