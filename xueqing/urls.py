"""xueqing URL Configuration

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
# from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.authtoken import views as rfauth_views
from rest_framework_jwt import views as rfjwt_views
from users import views as users_views
from general import views as general_views

router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'login', rfjwt_views.obtain_jwt_token)
router.register(r'users', users_views.UserViewSet, base_name='users')
router.register(r'account', users_views.AccountViewSet, base_name='account')
router.register(r'sms', users_views.SmsCodeViewSet, base_name='sms')

# 一件很重要的事情是：不要在后端写 Redirect，这回让前端路由不知所措

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name="index.html")),
    url(r'^api/v1/', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', rfauth_views.obtain_auth_token),
    path('api-jwt-auth/', rfjwt_views.obtain_jwt_token),
    path('api-webhook/', general_views.web_hook_view),
    path('test-webhook/', include(router.urls))
]