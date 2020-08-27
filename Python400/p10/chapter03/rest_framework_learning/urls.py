#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'rest_framework_learning'

urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
    path('groups/', views.GroupList.as_view()),
    path('groups/<int:pk>/', views.GroupDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
