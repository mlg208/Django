from django.db import models
from django.contrib.postgres.fields import ArrayField

class MyModel(models.Model):
    my_list = ArrayField(models.CharField(max_length=100), blank=True, null=True)
