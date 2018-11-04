from django.shortcuts import render
from django.conf.urls import url , include
from . import views
urlpatterns = [

    url(r'addnew', views.addnew, name='addnew'),
    url(r'^$', views.UserManagement , name = 'UserManagement'),
    url(r'^(?P<id>[0-9]+)/delete_user/$', views.delete_user11, name='delete_user11'),
    url(r'^(?P<id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<id>[0-9]+)/active/$', views.active, name='active'),
    url(r'^(?P<id>[0-9]+)/deactive/$', views.deactive, name='deactive'),

]