#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from . import views


urlpatterns = [
    path('var/', views.template_variables, name='template_variables'),
    path('for_and_if/', views.student_list, name='student_list'),
    path('filters/', views.filters, name='filters'),
]