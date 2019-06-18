from django.shortcuts import render
# from utils import http as utils_http
from utils import webhook as utils_webhook
# from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import list_route
from django_github_webhook.views import WebHookView

# Create your views here.

# def custom_exception_handler(exc, context):


def handler_404(request):
    # return HttpResponse("404您的页面找不到啦")
    # return utils_http.gen_error_response('请求的连接不存在', status.HTTP_404_NOT_FOUND)
    raise NotFound(detail="Error 404, page not found", code=404)

# class WebhookViewSet(viewsets.GenericViewSet):
#     permission_classes = [permissions.AllowAny]
#     @list_route(methods=['POST'],
#     serializer_class=WebhookSerializer)
#     def webhook(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return utils_http.gen_success_response()

class WebhookView(WebHookView):
    secret = utils_webhook.SECRET

    def push(self, payload, request):
        utils_webhook.do_reload()
        return {'status': 'received'}

web_hook_view = WebhookView.as_view()