from django.db import models
from django import forms
from django.contrib.auth.models import User
import MySQLdb
# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
class Deal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    deal_name = models.CharField(max_length=50)
    pipeline = models.CharField(max_length=50)
    deal_owner = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    close_day = models.CharField(max_length=50)
    
    def __str__(self):
        return(f"{self.deal_name}")
