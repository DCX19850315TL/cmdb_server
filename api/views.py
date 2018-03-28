# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# Create your views here.
def index(request):

    return HttpResponse('indexaaa')

@api_view(['GET','PUT','POST'])
def receive_server_info(request):

    print request.POST
    da = {'k1':[11,22,33,44]}

    return Response(json.dumps(da))

@api_view(['GET','PUT','DELETE','POST'])
def servers(request):

    method = request.method

    if method == 'POST':
        pass
    return  Response('ddddd')