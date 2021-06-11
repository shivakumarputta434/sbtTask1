from django.db import models


class Employee(models.Model):
    firstName=models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    salary = models.IntegerField(default=0)
    address = models.TextField(max_length=250)