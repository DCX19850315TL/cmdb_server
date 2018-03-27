# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    return HttpResponse('indexaaa')

def receive_server_info(request):

    print request.POST.get('data')

    return HttpResponse('test')