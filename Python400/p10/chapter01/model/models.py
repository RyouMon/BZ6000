from django.db import models

# Create your models here.


# many-to-one relationships
class Manufacture(models.Model):
    name = models.CharField(max_length=10)


class Car(models.Model):
    product = models.CharField(max_length=10)
    manufacture = models.ForeignKey('Manufacture', on_delete=models.CASCADE)


# many-to-many relationships
class Topping(models.Model):
    name = models.CharField(max_length=10)


class Pizza(models.Model):
    name = models.CharField(max_length=10)
    toppings = models.ManyToManyField(Topping)


# many-to-many relationships
# through a custom intermediary table
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
