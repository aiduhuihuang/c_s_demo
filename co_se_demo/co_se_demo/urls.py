"""co_se_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("set_cookie/",set_cookie),
    path("get_cookie/", get_cookie),
    path("del_cookie/", del_cookie),
    path("set_session/", set_session),
    path("get_session/", get_session),
    path("del_session/", del_session),
    path("login/",login),
    path("about/",about),
    path("loginout/",loginout),
    re_path("^$",index),#直接用ip和端口就可以进入的页面，首页需要登录的才能进入

]
