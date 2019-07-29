"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Employee(models.Model):

 name = models.CharField(max_length=150)
 lname = models.CharField(max_length=150)
 age = models.IntegerField()
 birthdate = models.CharField(max_length=150)
 department = models.CharField(max_length=150)
 updated = models.DateTimeField(auto_now=True)

def __unicode__(self):
    return self.name