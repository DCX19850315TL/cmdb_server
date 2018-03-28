#_*_ coding:utf-8 _*_
"""cmdb_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from api.views import index
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from api import models
from api import views

#=====User表的开始=====
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#=====User表的结束=====

# Serializers define the API representation.
class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Test
        fields = ('url','UserName','PassWord')

# ViewSets define the view behavior.
class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = TestSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tests', TestViewSet)

urlpatterns = [
    url(r'^index/',index),
    url(r'^server',views.servers),
    url(r'^', include(router.urls)),
]
