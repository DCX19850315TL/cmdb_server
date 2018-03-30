# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def put(request):
    #django.core.handlers.wsgi.WSGIRequest
    print request.POST
    print request.PUT
    print type(request)
    return HttpResponse('ok')
