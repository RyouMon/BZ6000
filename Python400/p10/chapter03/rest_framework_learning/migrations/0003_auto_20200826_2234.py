# Generated by Django 3.1 on 2020-08-26 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_learning', '0002_auto_20200826_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rest_framework_learning.group'),
        ),
    ]