"""MyDjanog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.login_action),
    url('^login.html/$', views.login_action),
    url('^login.html/$', views.logout, name='logout'),
    url('^login_action/$', views.login_action),
    url('^first_page/$', views.first_page),

    # 项目
    url('^project.html/$', views.get_projectitem, name='project'),
    url('^project_search/$', views.project_search),

    # 二级路由配置
    url('^functional_test/', include(('apps.functional_test.urls','functional_test'),namespace='functional_test')),
    url('^interface_test/', include(('apps.interface_test.urls','interface_test'),namespace= 'interface_test')),
    # path('performance_test/', include(('apps.performance_test.urls','performance_test'),namespace= 'performance_test')),
]
