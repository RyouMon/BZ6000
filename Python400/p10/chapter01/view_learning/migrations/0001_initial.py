# Generated by Django 3.0.8 on 2020-08-04 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=5)),
            ],
        ),
    ]
