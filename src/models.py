from django.db import models

# Create your models here.
class Internship(models.Model):
    fullname= models.CharField(max_length=100,null=True)
    email= models.EmailField()
    gender= models.CharField(max_length=50,null=True)
    qualification= models.CharField(max_length=200,null=True)
    year=models.IntegerField()
    contactno=models.IntegerField()
    institute= models.CharField(max_length=200,null=True)
    country= models.CharField(max_length=200,null=True)
    internshipdomain= models.CharField(max_length=200,null=True)
    duration= models.IntegerField()
    resume= models.FileField(upload_to='documents/')
    skills = models.TextField()
    experience = models.TextField(default='')