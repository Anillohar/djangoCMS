from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls import url , include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'dashboard/', views.dashboard , name='dashboard'),
    url(r'^$', TemplateView.as_view(template_name='html/welcome.html') ),
    url(r'UserManagement/', include('UserManagement.urls') ),
]