import random
import string
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    sex = models.IntegerField(choices=((1, 'Men'), (2, 'Women')), default=1)
    card_no = models.CharField(max_length=18)

    @classmethod
    def insert_test_data(cls, num=100):

        def random_str(chars, length):
            return ''.join(random.choices(chars, k=length))

        students = []
        for i in range(num):
            name = random_str(string.ascii_lowercase, 4)
            age = random.randint(18, 30)
            sex = random.choice([1, 2])
            card_no = random_str(string.digits, 18)
            students.append(Student(name=name, age=age, sex=sex, card_no=card_no))
        Student.objects.bulk_create(students)
