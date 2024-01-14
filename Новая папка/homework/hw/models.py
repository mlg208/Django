from django.db import models
from django.core.exceptions import ValidationError


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    value1 = models.IntegerField()
    value2 = models.IntegerField()

    def get_id_plus_value1(self):
        return f"{self.id} - {self.value1}"

    def get_sum_of_values(self):
        return self.value1 + self.value2

def validate_positive_number(value):
    if value < 0:
        raise ValidationError("Введите положительное число или 0.")


class My_Model(models.Model):
    name = models.CharField(max_length=100)
    value1 = models.IntegerField(validators=[validate_positive_number])
    value2 = models.IntegerField(validators=[validate_positive_number])
