#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from . import models


# class GroupRelateField(serializers.RelatedField):
#
#     def to_internal_value(self, data):
#         pass
#
#     def to_representation(self, value):
#         return {'id': value.id, 'level': value.level}


class StudentSerializer(serializers.ModelSerializer):

    # group = GroupRelateField(read_only=True)

    class Meta:
        model = models.Student
        # fields = ['id', 'name', 'age', 'sex', 'group']
        fields = ['id', 'name', 'age', 'sex']


# class GroupSerializer(serializers.ModelSerializer):
#
#     students = StudentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = models.Group
#         fields = ['id', 'level', 'students']
