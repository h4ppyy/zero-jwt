from django.urls import path
from django.conf.urls import url

from .restapi import views as restApiViews

urlpatterns = [
    path('', restApiViews.sample, name='sample'),

    path('api/v1/login', restApiViews.login, name='login'),
    path('api/v1/regist', restApiViews.regist, name='regist'),
    path('api/v1/saveFile', restApiViews.saveFile, name='saveFile'),

    path('test/randomLogin', restApiViews.randomLogin, name='randomLogin'),
    
    path('api/v1/saveValue', restApiViews.saveValue, name='saveValue'),
]
