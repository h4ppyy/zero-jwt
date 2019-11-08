from django.urls import path
from django.conf.urls import url

from .restapi import views as restApiViews

urlpatterns = [
    path('', restApiViews.sample, name='sample'),
]
