#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from . import views


app_name = 'rest_framework_learning'

urlpatterns = [
    path('students/', views.students),
    path('students/<int:pk>/', views.student_detail),
]
