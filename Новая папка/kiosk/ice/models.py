from django.db import models


class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.flavor

class IceCreamKiosk(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    ice_creams = models.ManyToManyField('IceCream', related_name='kiosks')

    def __str__(self):
        return self.name

class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Child(models.Model):
    name = models.CharField(max_length=100)
    parents = models.ManyToManyField('Parent', related_name='children')

    def __str__(self):
        return self.name


