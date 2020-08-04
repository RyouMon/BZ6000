#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('get/', views.MyView.as_view()),
    path('render/', views.test_render, name='test_render'),
    path('redirect/', views.test_redirect)
]
