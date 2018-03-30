#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
@author: tanglei
@contact: tanglei_0315@163.com
@file: http_request.py
@time: 2018/3/30 16:11
'''
from django.core.handlers.wsgi import WSGIRequest
from django.http.request import QueryDict
from io import BytesIO

class HttpRequest(WSGIRequest):

    @property
    def PUT(self):
        #根据body 获取数据
        #return 'PUT'
        if not hasattr(self, '_put'):
            self._load_put_and_files()
        return self._put

    def _load_put_and_files(self):
        """Populate self._post and self._files if the content-type is a form type"""
        if self.method != 'PUT':
            self._put = QueryDict(encoding=self._encoding)
            return
        if self._read_started and not hasattr(self, '_body'):
            self._mark_post_parse_error()
            return

        elif self.content_type == 'application/x-www-form-urlencoded':
            self._put = QueryDict(self.body, encoding=self._encoding)
        else:
            self._put = QueryDict(encoding=self._encoding)