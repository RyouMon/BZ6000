#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'rest_framework_learning'

urlpatterns = [
    path('students/', views.students),
    path('students/<int:pk>/', views.student_detail),
    path('groups/', views.groups),
    path('groups/<int:pk>/', views.group_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
