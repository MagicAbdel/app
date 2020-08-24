from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " " + self.lastname


class Child(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.lastname
