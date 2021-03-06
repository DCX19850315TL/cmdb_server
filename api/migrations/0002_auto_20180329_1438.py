# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=256, verbose_name='\u5bc6\u7801')),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=128, unique=True)),
                ('cabinet_num', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u673a\u67dc\u53f7')),
                ('cabinet_order', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u673a\u67dc\u4e2d\u5e8f\u53f7')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
                'verbose_name_plural': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
        migrations.CreateModel(
            name='Business_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u4e1a\u52a1\u7ebf')),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='\u5408\u540c\u53f7')),
                ('name', models.CharField(max_length=64, verbose_name='\u5408\u540c\u540d')),
                ('cost', models.IntegerField(verbose_name='\u5408\u540c\u91d1\u989d')),
                ('start_date', models.DateTimeField(blank=True, verbose_name='\u5408\u540c\u8d77\u59cb\u65f6\u95f4')),
                ('end_date', models.DateTimeField(blank=True, verbose_name='\u5408\u540c\u7ed3\u675f\u65f6\u95f4')),
                ('license_num', models.IntegerField(blank=True, verbose_name='license\u6570\u91cf')),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5408\u540c',
                'verbose_name_plural': '\u5408\u540c',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=128, verbose_name='CPU\u578b\u53f7')),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'CPU\u90e8\u4ef6',
                'verbose_name_plural': 'CPU\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(blank=True, max_length=128, verbose_name='\u63d2\u69fd\u4f4d')),
                ('enclosure', models.CharField(blank=128, max_length=128, null=True, verbose_name='\u9644\u4ef6')),
                ('model', models.CharField(blank=True, max_length=128, verbose_name='\u78c1\u76d8\u578b\u53f7')),
                ('capacity', models.FloatField(blank=True, verbose_name='\u78c1\u76d8\u5bb9\u91cf')),
                ('iface_type', models.CharField(blank=True, max_length=128, verbose_name='\u63a5\u53e3\u7c7b\u578b')),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u78c1\u76d8\u90e8\u4ef6',
                'verbose_name_plural': '\u78c1\u76d8\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='HandleLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Handle_type', models.CharField(blank=True, max_length=256, verbose_name='\u5904\u7406\u7c7b\u578b')),
                ('summary', models.CharField(blank=True, max_length=256, verbose_name='\u5904\u7406\u7684\u603b\u6570')),
                ('detail', models.TextField(verbose_name='\u5904\u7406\u7684\u8be6\u7ec6\u4fe1\u606f')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_display_name', models.CharField(default=None, max_length=64, verbose_name='\u533a\u57df\u540d\u79f0')),
                ('display_name', models.CharField(default=None, max_length=64, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('floor', models.IntegerField(default=1, verbose_name='\u697c\u5c42')),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='\u7f51\u5361\u540d\u79f0')),
                ('model', models.CharField(blank=True, max_length=128, verbose_name='\u7f51\u5361\u578b\u53f7')),
                ('ipaddrs', models.GenericIPAddressField(verbose_name='IP\u5730\u5740')),
                ('mac', models.CharField(blank=True, max_length=128, verbose_name='\u7f51\u5361mac\u5730\u5740')),
                ('netmask', models.CharField(blank=True, max_length=128, verbose_name='\u5b50\u7f51\u63a9\u7801')),
                ('gateway', models.CharField(blank=True, max_length=128, verbose_name='\u7f51\u5173')),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u7f51\u5361\u90e8\u4ef6',
                'verbose_name_plural': '\u7f51\u5361\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=64, verbose_name='SN\u53f7')),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5236\u9020\u5546')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u578b\u53f7')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Asset')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='Tag name')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u540d\u5b57')),
                ('email', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=32, verbose_name='\u5ea7\u673a')),
                ('mobile', models.CharField(max_length=32, verbose_name='\u624b\u673a')),
                ('memo', models.TextField(blank=True, verbose_name='\u5907\u6ce8')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='tag',
            name='creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server'),
        ),
        migrations.AddField(
            model_name='handlelog',
            name='creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='server_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Server'),
        ),
        migrations.AddField(
            model_name='business_unit',
            name='contact',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Business_unit', verbose_name='\u5c5e\u4e8e\u7684\u4e1a\u52a1\u7ebf'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Contract', verbose_name='\u5408\u540c'),
        ),
        migrations.AddField(
            model_name='asset',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DeviceType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.IDC', verbose_name='IDC\u673a\u623f'),
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Status'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(to='api.Tag'),
        ),
        migrations.AddField(
            model_name='asset',
            name='userpro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.UserProfile', verbose_name='\u8bbe\u5907\u7ba1\u7406\u5458'),
        ),
        migrations.AddField(
            model_name='admininfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.UserProfile'),
        ),
        migrations.AlterIndexTogether(
            name='server',
            index_together=set([('sn', 'asset')]),
        ),
    ]
