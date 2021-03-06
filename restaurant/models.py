# -*- coding: utf-8 -*-
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=3,decimal_places=0)
    comment = models.CharField(max_length=50, blank=True)
    is_spicy = models.BooleanField()
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name# Create your models here.

    def __str__(self):
        return self.name
class Comment(models.Model):
    content = models.CharField(max_length=200)
    user = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
