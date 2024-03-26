from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Record(models.Model):
    first_name=models.CharField(max_length=200,blank=True)
    last_name=models.CharField(max_length=140)
    email=models.EmailField()
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return  self.first_name + " "+self.last_name
class ProfileInfo(models.Model):
   user=models.OneToOneField(User,on_delete=models.CASCADE)

   portfolio=models.URLField(blank=True)

   def __str__(self):
      return self.user.username
          