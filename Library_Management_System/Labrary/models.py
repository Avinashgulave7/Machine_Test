from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    book_name=models.CharField(max_length=100,blank=True)
    createon = models.DateTimeField(auto_now_add=True)
    modifedon = models.DateTimeField(auto_now_add=True)

