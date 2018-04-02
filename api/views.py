# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from api import models
from django.shortcuts import render_to_response
from api.models import Test

# Create your views here.
def index(request):

    return HttpResponse('indexaaa')

@api_view(['GET','PUT','POST'])
def receive_server_info(request):
    #解析Agent发过来的数据
    #数据库中没有数据，保存数据到数据库
    #数据库中有数据，更新数据库中的数据，所有操作都记录到HandleLog的表里面
    server_info = request.POST.get('data')
    server_info = server_info.encode('utf=8')
    server_info_dict = json.loads(server_info)
    print server_info_dict
    hostname = server_info_dict['hostname']
    if server_info_dict['modify'] == 0:
        #资产表更新列
        pass
    else:
        flag = server_info_dict['nic']['mondify']
        if flag == 0:
            pass
        else:
            #通过hostname找到资产，通过资产找到对应的服务器==ID
            #通过服务器的ID找到对应的网卡信息
            old_nic_list = models.NIC.object.filter(server__id=1)
            #比较两个循环，插槽
            for item in old_nic_list:
                for new_key,new_value in server_info_dict['nic']['data'].items:
                    if item.name == new_key:
                        if item.ipaddrs != new_value['ipaddres']:
                            log_info = '网卡%sIP由[%s]变更为[%s]' %(item.name,item.ipaddrs,new_value['ipaddres'])
                            #将操作日志写入到HandleLog表中，用户名:cmdb_report
                            item.ipaddrs = new_value['ipaddres']
                            item.save()



    #print request.POST
    #da = {'k1':[11,22,33,44]}
    #return Response(json.dumps(da))

@api_view(['GET','PUT','DELETE','POST'])
def servers(request):

    method = request.method

    if method == 'POST':
        pass
    return  Response('ddddd')

def TestsList(request):
    #获取test表里面的所有数据
    tests_list = Test.objects.all()

    #把数据嵌套在html中
    #再把新的大字符串返回给客户端
    result = render_to_response('test.html',{'data':tests_list,'user':'tanglei'})
    return  result

def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        print user,pwd
        return render_to_response('login.html')
    else:
        return render_to_response('login.html')

