#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.dispatch import Signal, receiver


index_signal = Signal(providing_args=['request'])


@receiver(index_signal, dispatch_uid='pre_index_request')
def pre_index_request(sender, request=None, **kwargs):
    print(f'访问首页之前：{sender}, {kwargs}')
    print('访问IP：', request.META['REMOTE_ADDR'])


def pre_save_receive(sender, **kwargs):
    print(f'模型保存之前：{sender}, kwargs: {kwargs}')
