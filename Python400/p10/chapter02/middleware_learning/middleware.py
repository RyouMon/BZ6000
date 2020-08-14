#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin


class FirstMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__.__name__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__.__name__}: process response')
        return response

    def process_template_response(self, request, response):
        print(f'{self.__class__.__name__}: process template response')
        return response


class SecondMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__.__name__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__.__name__}: process response')
        return response

    def process_template_response(self, request, response):
        print(f'{self.__class__.__name__}: process template response')
        response.context_date = {'msg': 'Here is a Massage from SecondMiddleware'}
        return response


class ThirdMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__.__name__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__.__name__}: process response')
        return response

    def process_template_response(self, request, response):
        print(f'{self.__class__.__name__}: process template response')
        return response
