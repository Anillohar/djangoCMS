from django.conf.urls import url
from admin_panel import views

urlpatterns = [
    url(r'login/', views.login, name='login'),
    url(r'forgot_password/', views.forgot_password, name='forgot_password'),
]