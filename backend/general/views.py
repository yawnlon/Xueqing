from django.shortcuts import render
from utils import http as utils_http
from utils import webhook as utils_webhook
from utils import permissions as utils_permissions
from utils import paginations as utils_paginations
from users.serializers import SelfVerifySerializer
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework import filters
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import list_route
from django_github_webhook.views import WebHookView
from rest_framework import viewsets
from django.views.generic import View
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.

def handler_404(request):
    # return HttpResponse("404您的页面找不到啦")
    # return utils_http.gen_error_response('请求的连接不存在', status.HTTP_404_NOT_FOUND)
    raise NotFound(detail="Error 404, page not found", code=404)

class GithubWebhookView(WebHookView):
    secret = utils_webhook.SECRET

    def push(self, payload, request):
        utils_webhook.reload()
        return {'detail': 'Success!!'}

class GiteeWebhookView(View):
    secret = utils_webhook.SECRET

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        secret = self.secret
        if not secret:
            raise utils_http.APIException400('Webhook secret ist not defined.')
        if 'HTTP_X_GITEE_TOKEN' not in request.META:
            return HttpResponseBadRequest('Request does not contain HTTP_X_GITEE_TOKEN header')
        if request.META['HTTP_X_GITEE_TOKEN'] != secret:
            return HttpResponseBadRequest('Password Wrong!')
        if 'HTTP_X_GITEE_EVENT' not in request.META:
            return HttpResponseBadRequest('Request does not contain HTTP_X_GITEE_EVENT header')
        if request.META['HTTP_X_GITEE_EVENT'] != 'Push Hook':
            HttpResponseBadRequest('Event does not Support!')
        utils_webhook.reload()
        return JsonResponse({'detail': 'Success!!'})
         
github_web_hook_view = GithubWebhookView.as_view()
gitee_web_hook_view = GiteeWebhookView.as_view()

class XQModelViewSet(viewsets.ModelViewSet):
    authentication_classes=[JSONWebTokenAuthentication]
    pagination_class = utils_paginations.XQPagination
    filter_backends = (filters.SearchFilter,)
    
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
        instance = self.get_object()
        self.perform_destroy(instance)
        return utils_http.gen_success_response(msg="删除成功", 
            status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return utils_http.gen_success_response(data=serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return utils_http.gen_success_response(data=serializer.data)

    def get_permissions(self):
        return [utils_permissions.IsAdminOrReadOnly()]

class AdminModelViewSet(XQModelViewSet):

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return super().destroy(self, request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action == 'destroy':
            return SelfVerifySerializer
        return self.serializer_class