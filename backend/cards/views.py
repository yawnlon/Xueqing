from django.shortcuts import render
from rest_framework import permissions
from rest_framework import status
from .models import StudyCard
from .serializers import StudyCardSerializer
from users.serializers import SelfVerifySerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils import permissions as utils_permissions
from utils import http as utils_http
from general.views import AdminModelViewSet

# Create your views here.

class StudyCardViewSet(AdminModelViewSet):
    queryset = StudyCard.objects.all()
    serializer_class = StudyCardSerializer
    # def list(self, request, *args, **kwargs):
