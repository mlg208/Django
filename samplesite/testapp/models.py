from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import DateTimeRangeField, ArrayField, HStoreField, CICharField, JSONField
from django.contrib.postgres.indexes import GistIndex
from django.db import models
from django.contrib.auth.models import User    # permission и все что с ним связано взял из gpt


# class Group(models.Model):
#     group = Group.objects.create(name='Доступ')
#     superuser_permission = Permission.objects.get(codename='superuser')
#     group.permisions.add(superuser_permission)

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

class PGSRoomReserving(models.Model):
    name = models.CharField(max_length=30, verbose_name='помещение')
    reserving = DateTimeRangeField(verbose_name='Время резервирования')
    cancelled = models.BooleanField(default=False, verbose_name='отменить резервирование')

class PGSRubric(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    tags = ArrayField(base_field=models.CharField(max_length=20), verbose_name='Теги')

    class Meta:
        indexes = [
            GistIndex(fields=['reserving'],
                        name='i_pgsrr_reserving',
                        opclasses=('range_ops',),
                        fillfactor=50)
        ]
class PGSProject(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    platform = ArrayField(base_field=ArrayField(
        base_field=models.CharField(max_length=20)),
        verbose_name='Используемые платформы'
    )

class PGSProject2(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')
    platforms = HStoreField(verbose_name='Используемые платформы')

class PGSProject3(models.Model):
    name = CICharField(max_length=40, verbose_name='Название')
    data = JSONField()

