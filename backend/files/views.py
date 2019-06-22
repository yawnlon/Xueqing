from django.shortcuts import render
from utils import qncloud as utils_qn
from utils import http as utils_http
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import list_route
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.

class QiniuViewSet(viewsets.GenericViewSet):

    @list_route(methods=['GET'],
        authentication_classes=[JSONWebTokenAuthentication],
        permission_classes=[permissions.IsAuthenticated],
        url_path="upload-token")
    def upload_token(self, request, *args, **kwargs):
        token = utils_qn.gen_token()
        return utils_http.gen_success_response(data={
            "token": token
        })