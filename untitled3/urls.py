from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from django.conf.urls import url
urlpatterns = [
  #  path('', include('admin_panel.urls')),
    url(r'^admin/', include('admin_panel.urls')),
    url(r'^admin/',include('admin.urls')),
    url(r'^$' , include('admin.urls')),
    url(r'^admin/settings/' , include('settings.urls')),
               ]