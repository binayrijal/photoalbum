from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Album(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='image',null=True,blank=True)
    classification=models.CharField(max_length=50)
    
