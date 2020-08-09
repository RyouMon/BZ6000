#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


app_name = 'paginator_learning'

urlpatterns = [
    path('students/', views.student_list, name='students'),
    path('students/<int:page>', views.student_list, name='student_list'),
]
