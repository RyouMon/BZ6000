# Generated by Django 3.1 on 2020-08-28 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_learning', '0003_auto_20200826_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]