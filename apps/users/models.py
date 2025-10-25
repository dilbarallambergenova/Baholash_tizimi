from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.assignments.models import Group

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', "O'quvchi"),
        ('teacher', "O'qituvchi"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    group=models.ForeignKey(Group,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"