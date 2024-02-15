from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from django.contrib.auth.models import User


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Spare(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

class Engine(models.Model):
    name = models.CharField(max_length=30)

class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare, through='Kit',
                                    through_fields=('machine', 'spare'))
    notes = GenericRelation('Note')

    def __str__(self):
        return f'{self.name}'


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)


class Note(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(ct_field='content_type', fk_field='object_id')


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=40)
    model = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.make} {self.model} ({self.owner.username})'     #строку украл из гпт


class SparePart(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name     #и эту тоже


class CarSparePart(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('car', 'spare_part')

    def __str__(self):
        return f'{self.car} - {self.spare_part}: {self.quantity}'     #и снова взял из гпт


class Message(models.Model):
    content = models.TextField()


class PrivateMessage(Message):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # message = models.OneToOneField(Message, on_delete=models.CASCADE, parent_link=True)


# class BaseMessage(models.Model):
#     content = models.TextField()
#
#     class Meta:
#         abstract = True
#
#
# class Message(BaseMessage):
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#
#
# class PrivateMessage(BaseMessage):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#
#     class Meta:
#         verbose_name = 'Private Message'
#
#
# class GeneralMessage(PrivateMessage):
#     email = models.EmailField()
#
#     class Meta:
#         verbose_name = 'General Message'

# class Message(models.Model):
#     content = models.TextField()
#     name = models.CharField(max_length=20)
#     email = models.EmailField()
#
#     class Meta:
#         sbstract = True
#
# class PrivateMessage(Message):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#     email = None
#
#     class Meta(Message.Meta):
#         pass
