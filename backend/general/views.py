from django.shortcuts import render
# from utils import http as utils_http
# from rest_framework import status
from rest_framework.exceptions import NotFound

# Create your views here.

# def custom_exception_handler(exc, context):


def handler_404(request):
    # return HttpResponse("404您的页面找不到啦")
    # return utils_http.gen_error_response('请求的连接不存在', status.HTTP_404_NOT_FOUND)
    raise NotFound(detail="Error 404, page not found", code=404)