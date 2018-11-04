from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from django.conf.urls import url
from . import views
from django.utils.translation import ugettext_lazy

urlpatterns = [
    url(r'edit-settings/(?P<id>[0-9]+)', views.editsettings, name='editsettings'),
    url(r'add-settings', views.addsettings, name='addsettings'),
    url(r'(?P<id>[0-9]+)/delete-settings' , views.deletesettings , name='deletesettings'),
    url(r'prefix/reading', views.sitesettingsmain, name='reading'),
    url(r'prefix/site', views.sitesettingsmain, name='site'),
    url(r'prefix/social', views.sitesettingsmain, name='social'),
    url(r'prefix/defaultlanguage', views.sitesettingsmain, name='default_language'),
    url(r'prefix/email', views.sitesettingsmain, name='email'),
    url(r'prefix', views.sitesettingsmain, name='prefix'),
    url(r'', views.settings , name= 'settings'),
]

