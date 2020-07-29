#!/usr/bin/env python
# -*-coding:utf-8-*-
from django.urls import path, re_path, register_converter
from . import views, converters


register_converter(converters.FourDigitYearConverter, 'yyyy')


urlpatterns = [
    path('', views.index),
    path('2003', views.special_case_2003),
    # path('<int:year>', views.year_archive),
    # path('<int:year>/<int:mouth>', views.mouth_archive),
    # path('<int:year>/<int:mouth>/<slug:slug>', views.article_detail),
    # path('<yyyy:year>', views.year_archive),
    # path('<yyyy:year>/<int:mouth>', views.mouth_archive),
    # path('<yyyy:year>/<int:mouth>/<slug:slug>', views.article_detail),
    re_path(r'^(?P<year>\d{4})/$', views.year_archive),
    re_path(r'^(?P<year>\d{4})/(?P<mouth>\d{2})/$', views.mouth_archive),
    re_path(r'^(?P<year>\d{4})/(?P<mouth>\d{2})/(?P<slug>[\w-]+)/$', views.article_detail),
    path('blog/', views.page),
    path('blog/page-<int:num>/', views.page)
]
