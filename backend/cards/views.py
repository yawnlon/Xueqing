from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from .models import StudyCard
from .serializers import StudyCardSerializer
from users.serializers import SelfVerifySerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils import permissions as utils_permissions
from utils import http as utils_http

# Create your views here.

class StudyCardViewSet(viewsets.ModelViewSet):
    queryset = StudyCard.objects.all()
    # serializer_class = StudyCardSerializer
    authentication_classes=[JSONWebTokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return utils_http.gen_success_response(msg="创建成功", 
            data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return utils_http.gen_success_response(msg="修改成功", 
            data=serializer.data)

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils_http.gen_success_response(msg="删除成功", 
            status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'destroy':
            return SelfVerifySerializer
        return StudyCardSerializer

    def get_permissions(self):
        return [utils_permissions.IsAdminOrReadOnly()]

    # def list(self, request, *args, **kwargs):
