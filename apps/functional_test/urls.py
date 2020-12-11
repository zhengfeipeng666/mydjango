# -*- coding: utf-8 -*-
# @Time : 2020/12/8 11:09
# @Author : wangchao
# @Email : wangchao8@tiens.com
# @File : urls.py
# @Project : MyDjanog

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.functional_test import views


urlpatterns = [
    # 测试模块
    url('get_modules/$',views.get_modules,name='get_modules'),

]