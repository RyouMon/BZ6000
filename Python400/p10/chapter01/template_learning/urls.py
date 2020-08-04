#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from . import views


urlpatterns = [
    path('var/', views.template_variables, name='template_variables'),
]