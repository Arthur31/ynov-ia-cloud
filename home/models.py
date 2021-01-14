from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Profile(models.Model):
    user = models.OneToOneField(Project, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    creation_date = models.DateTimeField() 