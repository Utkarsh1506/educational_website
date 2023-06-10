from django.db import models
from django.contrib.auth.models import User

    

class Contact(models.Model):
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)


    
class Class_9th(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    maths = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()
    hindi = models.IntegerField()
    social_science = models.IntegerField()
    
class Class_10th(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    maths = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()

class Class_11th(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    english = models.IntegerField()
    computer_science = models.IntegerField()
    biology = models.IntegerField()
    physical_education = models.IntegerField()
    
class Class_12th(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    english = models.IntegerField()
    computer_science = models.IntegerField()
    biology = models.IntegerField()
    physical_education = models.IntegerField()
    
class Bsc(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    
class Btech(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    maths = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    
class Skill(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    skill_1 = models.CharField(max_length=100)
    skill_2 = models.CharField(max_length=100)
    skill_3 = models.CharField(max_length=100)
    
class Course(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    class_9th = models.CharField(max_length=100)
    class_10th = models.CharField(max_length=100)
    class_11th = models.CharField(max_length=100)
    class_12th = models.CharField(max_length=100)
    bsc = models.CharField(max_length=100)
    btech = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    
    
    
class Student(User):
    
    def __str__(self):
        return 'Message from ' + self.email


