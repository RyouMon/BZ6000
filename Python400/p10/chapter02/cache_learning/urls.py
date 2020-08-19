#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from . import views

urlpatterns = [
    path('site/', views.per_site_cache),
]
