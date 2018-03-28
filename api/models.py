# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Test(models.Model):

    UserName = models.CharField(max_length=255)

    PassWord = models.CharField(max_length=255)

#cmdb数据库设计
#普通用户表
class UserProfile(models.Model):
    name = models.CharField(u'名字',max_length=32)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'座机',max_length=32)
    mobile = models.CharField(u'手机',max_length=32)
    memo = models.TextField(u'备注',blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    def __unicode__(self):
        return self.name

#管理员用户表，需要和普通用户表做一一对应的关系，一个管理员用户只能对应一个普通用户
class AdminInfo(models.Model):
    user = models.OneToOneField(UserProfile)
    username = models.CharField(u'用户名',max_length=256)
    password = models.CharField(u'密码',max_length=256)

#设备类型表，如：服务器，交换机等
class DeviceType(models.Model):
    name = models.CharField(max_length=64)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备资产表
class Asset(models.Model):
    device_type = models.ForeignKey('DeviceType')
    hostname = models.CharField(max_length=128,blank=True,unique=True)
    cabinet_num = models.CharField(u'机柜号',max_length=30,null=True,blank=True)
    cabinet_order = models.CharField(u'机柜中序号',max_length=30,null=True,blank=True)

#存储服务器设备的表
class Server(models.Model):

#存储网络设备的表
class NetworkDevice(models.Model):