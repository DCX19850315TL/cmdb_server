# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Test(models.Model):

    UserName = models.CharField(max_length=255)

    PassWord = models.CharField(max_length=255)

    create_at = models.DateTimeField(blank=True,auto_now_add=True)

    update_at = models.DateTimeField(blank=True,auto_now=True)

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
        verbose_name_plural = "用户信息"
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

#服务器的状态，如：线上，测试，临时外借
class Status(models.Model):
    name = models.CharField(max_length=64)
    memo = models.TextField(u'备注',null=True,blank=True)

#设备资产表
class Asset(models.Model):
    device_type = models.ForeignKey('DeviceType')
    status = models.ForeignKey('Status')
    hostname = models.CharField(max_length=128,blank=True,unique=True)
    cabinet_num = models.CharField(u'机柜号',max_length=30,null=True,blank=True)
    cabinet_order = models.CharField(u'机柜中序号',max_length=30,null=True,blank=True)
    memo = models.TextField(u'备注',null=True,blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    idc = models.ForeignKey('IDC',verbose_name=u'IDC机房',null=True,blank=True)
    contract = models.ForeignKey('Contract',verbose_name=u'合同',null=True,blank=True)
    business_unit = models.ForeignKey('Business_unit',verbose_name=u'属于的业务线',null=True,blank=True)
    userpro = models.ForeignKey('UserProfile',verbose_name=u'设备管理员',related_name='+',null=True,blank=True)
    tag = models.ManyToManyField('Tag')
    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"

    def __unicode__(self):
        return 'id:%s h:%s' %(self.id,self.hostname)


#存储服务器设备的表
class Server(models.Model):
    asset = models.OneToOneField('Asset')
    sn = models.CharField(u'SN号',max_length=64)
    manufactory = models.CharField(verbose_name=u'制造商',max_length=64,null=True,blank=True)
    model = models.CharField(u'型号',max_length=128,null=True,blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"
        index_together = ["sn","asset"]

    def __unicode__(self):
        return '%s sn:%s' %(self.asset.hostname,self.sn)

#存储网络设备的表
#class NetworkDevice(models.Model):
#    pass

#存储CPU信息的表
class CPU(models.Model):
    model = models.CharField(u'CPU型号',max_length=128,blank=True)
    memo = models.TextField(u'备注',blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    server_info = models.ForeignKey('Server')
    class Meta:
        verbose_name = 'CPU部件'
        verbose_name_plural = "CPU部件"
    def __unicode__(self):
        return '%s' %(self.model)

#存储内存信息的表
#class Memory(models.Model):
#    pass

#存储硬盘信息的表
class Disk(models.Model):
    slot = models.CharField(u'插槽位',max_length=128,blank=True)
    enclosure = models.CharField(u'附件',max_length=128,blank=128,null=True)
    model = models.CharField(u'磁盘型号',max_length=128,blank=True)
    capacity = models.FloatField(u'磁盘容量',blank=True)
    iface_type = models.CharField(u'接口类型',max_length=128,blank=True)
    memo = models.TextField(u'备注',blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    server_info = models.ForeignKey('Server')
    class Meta:
        verbose_name = '磁盘部件'
        verbose_name_plural = "磁盘部件"

    def __unicode__(self):
        return '%s %s %s %s' %(self.slot,self.model,self.capacity,self.iface_type)


#存储网卡信息的表
class NIC(models.Model):
    name = models.CharField(u'网卡名称',max_length=128,blank=True)
    model = models.CharField(u'网卡型号',max_length=128,blank=True)
    ipaddrs = models.GenericIPAddressField(u'IP地址')
    mac = models.CharField(u'网卡mac地址',max_length=128,blank=True)
    netmask = models.CharField(u'子网掩码',max_length=128,blank=True)
    gateway = models.CharField(u'网关',max_length=128,blank=True)
    memo = models.TextField(u'备注',blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    server_info = models.ForeignKey('Server')
    class Meta:
        verbose_name = '网卡部件'
        verbose_name_plural = "网卡部件"
    def __unicode__(self):
        return '%s:%s' %(self.name,self.ipaddrs)


#存储合同的表
class Contract(models.Model):
    sn = models.CharField(u'合同号',max_length=64,unique=True)
    name = models.CharField(u'合同名',max_length=64)
    cost = models.IntegerField(u'合同金额')
    start_date = models.DateTimeField(u'合同起始时间',blank=True)
    end_date = models.DateTimeField(u'合同结束时间',blank=True)
    license_num = models.IntegerField(u'license数量',blank=True)
    memo = models.TextField(u'备注',blank=True)
    create_at = models.DateTimeField(u'创建时间',blank=True,auto_now_add=True)
    update_at = models.DateTimeField(u'更新时间',blank=True,auto_now=True)
    class Meta:
        verbose_name = '合同'
        verbose_name_plural = "合同"
    def __unicode__(self):
        return self.name

#存储业务线的表
class Business_unit(models.Model):
    name = models.CharField(u'业务线',max_length=64,unique=True)
    contact = models.ForeignKey('UserProfile',default=None)
    memo = models.TextField(u'备注',blank=True)
    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = "业务线"
    def __unicode__(self):
        return self.name

#存储IDC的表
class IDC(models.Model):
    region_display_name = models.CharField(u'区域名称',max_length=64,default=None)
    display_name = models.CharField(u'机房名称',max_length=64,default=None)
    floor = models.IntegerField(u'楼层',default=1)
    memo = models.TextField(u'备注',blank=True)
    class Meta:
        verbose_name = '机房'
        verbose_name_plural = "机房"
    def __unicode__(self):
        return 'region:%s idc:%s floor:%s' % (self.region_display_name,self.display_name,self.floor)

#存储服务器的标识的表，如：运行用户中心的服务器
class Tag(models.Model):
    name = models.CharField('Tag name',max_length=64,blank=True)
    creater = models.ForeignKey('UserProfile')
    def __unicode__(self):
        return self.name

#存储变更的日志记录表
class HandleLog(models.Model):
    Handle_type = models.CharField(u'处理类型',max_length=256,blank=True)
    summary = models.CharField(u'处理的总数',max_length=256,blank=True)
    detail = models.TextField(u'处理的详细信息')
    creater = models.ForeignKey('UserProfile')
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_now=True)
    memo = models.TextField(u'备注',blank=True)