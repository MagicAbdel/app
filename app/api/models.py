from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Parent(models.Model):
    name = models.CharField(max_length=200, validators=[RegexValidator('^[a-zA-Z]+$')])
    lastname = models.CharField(max_length=200, validators=[RegexValidator('^[a-zA-Z]+$')])

    street = models.CharField(max_length=200, validators=[RegexValidator('^[a-zA-Z0-9]+$')])
    city = models.CharField(max_length=200, validators=[RegexValidator('^[a-zA-Z]+$')])
    zipcode = models.IntegerField(validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    state = models.CharField(max_length=200, validators=[RegexValidator('^[a-zA-Z]+$')])

    def __str__(self):
        return self.name + " " + self.lastname


class Child(models.Model):
    name = models.CharField(max_length=200, validators=[RegexValidator('^[a-zA-Z]+$')])
    lastname = models.CharField(max_length=200, validators=[RegexValidator('^[a-zA-Z]+$')])

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.lastname
