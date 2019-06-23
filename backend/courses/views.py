from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from users.serializers import SelfVerifySerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils import permissions as utils_permissions
from utils import http as utils_http
from general.views import AdminModelViewSet

# Create your views here.

class CourseViewSet(AdminModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 
    search_fields = ('name', 'code')   