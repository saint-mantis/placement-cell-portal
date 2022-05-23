from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    password = models.CharField(max_length=100)
    internship = ArrayField(models.CharField(max_length=100),blank=True,null=True)
    companyinput = models.CharField(max_length=100)
    


    def __str__(self):
        return self.name

class Companies(models.Model):
    companyname = models.CharField(max_length=1000)
    addcompany = models.CharField(max_length=100)

    def __str__(self):
        return self.companyname