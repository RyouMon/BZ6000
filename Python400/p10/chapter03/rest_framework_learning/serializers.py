#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = ['id', 'name', 'age', 'sex']
