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
    path('admin/', admin.site.urls),
    # url('^functional_test/$',include('functional_test.urls')),

]