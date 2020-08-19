#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('site/', views.per_site_cache),
    path('view/', views.view),
    path('cached_view/', cache_page(60)(views.cached_view)),
]
