from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.TextField()
    education=models.TextField(null=True)
    skills=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="myimage")
    projects=models.TextField(null=True)
    
