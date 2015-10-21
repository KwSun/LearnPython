"""LearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
import web.urls

def active(request):
    #获取URL
    #1、app名字
    #2、file名字
    #3、函数名
    pass

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url ---Function
#     '''
#     url(r'^index/', index),
# #     url(r'^list/(?P<name>\d*)/(?P<id>\d*)/$', lists),
#     url(r'^list/(?P<name>\d*)/$', lists,{'id':123}),
#     '''
    #url ---file
    #file ---url ---> Function
   # url(r'^web/', web.urls),
    url(r'^web/', include(web.urls)),


]
