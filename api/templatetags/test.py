#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: test.py
@time: 2018/4/1 16:32
'''
# !/usr/bin/env python
# coding:utf-8
from django import template
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()

@register.simple_tag
def mymethod(v1):
    result = v1*1000
    return result