from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
#import wallet_app.wallet_task as wallet_task

# Create your models here.



class wallet(models.Model):  
    id = models.IntegerField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    #user_name = models.CharField(max_length=50)
    #password = models.CharField(max_length=50)
    activated = models.BooleanField(default=False)
    balance = models.FloatField(max_length=20, default=0)
    transacations = []

class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    #email = models.EmailField(validators=[wallet_task.validate_gmail])
    #phone_no =models.CharField(max_length=15,validators=[wallet_task.validate_phone_no])




