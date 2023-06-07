from django.db import models
from django.contrib.auth.models import User

    

class Contact(models.Model):
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

class Student(User):
    
    
    def __str__(self):
        return 'Message from ' + self.email


