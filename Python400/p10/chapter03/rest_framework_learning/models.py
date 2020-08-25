from django.db import models

# Create your models here.


class Student(models.Model):
    SEX_CHOICES = ((0, 'Male'), (1, 'Female'))

    name = models.CharField(max_length=20, verbose_name='Name')
    age = models.IntegerField(null=True, blank=True, verbose_name='Age')
    sex = models.IntegerField(choices=SEX_CHOICES, default=0, verbose_name='Sex')
