# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Product(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    image = models.FileField()

    def get_absolute_url(self):
        return reverse('products-list', kwargs={})

    def __str__(self):
        return self.manufacturer + '  ' + self.name


class Customers(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    middle_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    phone_number = models.CharField(default='+380XXXXXXXXX', max_length=13, null=False, blank=False)





