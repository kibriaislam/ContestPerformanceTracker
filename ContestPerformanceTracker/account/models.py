from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    codeforcesid=models.CharField(max_length=250,unique=True)
    uvaid=models.CharField(max_length=250,unique=True)
    githubid=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.user.username
    
    
