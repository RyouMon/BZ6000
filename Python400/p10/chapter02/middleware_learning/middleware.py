#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class FirstMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__.__name__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__.__name__}: process response')
        return response

    def process_template_response(self, request, response):
        print(f'{self.__class__.__name__}: process template response')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'{self.__class__.__name__}: process view')

    def process_exception(self, request, exception):
        # This method will not be called.
        print(f'{self.__class__.__name__}: process exception')


class SecondMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__.__name__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__.__name__}: process response')
        return response

    def process_template_response(self, request, response):
        print(f'{self.__class__.__name__}: process template response')
        response.context_data = {'msg': 'Here is a Massage from SecondMiddleware'}
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'{self.__class__.__name__}: process view')
        # return view_func(request)

    def process_exception(self, request, exception):
        print(f'{self.__class__.__name__}: process exception')
        return HttpResponse(f'Catch an exception: {exception!r}')


class ThirdMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f'{self.__class__.__name__}: process request')

    def process_response(self, request, response):
        print(f'{self.__class__.__name__}: process response')
        return response

    def process_template_response(self, request, response):
        print(f'{self.__class__.__name__}: process template response')
        print(response.is_rendered)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(f'{self.__class__.__name__}: process view')

    def process_exception(self, request, exception):
        print(f'{self.__class__.__name__}: process exception')
