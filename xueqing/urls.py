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
from users import views as uv

router = routers.DefaultRouter()
router.register(r'users', uv.UserViewSet)
router.register(r'groups', uv.GroupViewSet)

# 一件很重要的事情是：不要在后端写 Redirect，这回让前端路由不知所措

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name="index.html")),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]
