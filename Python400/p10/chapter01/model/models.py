from django.db import models

# Create your models here.


# many-to-one relationships
class Manufacture(models.Model):
    name = models.CharField(max_length=10)


class Car(models.Model):
    product = models.CharField(max_length=10)
    manufacture = models.ForeignKey('Manufacture', on_delete=models.CASCADE)
