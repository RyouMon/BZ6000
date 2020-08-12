#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin


class FirstMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__}: process response')
        return response


class SecondMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__}: process response')
        return response


class ThirdMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__}: process response')
        return response
