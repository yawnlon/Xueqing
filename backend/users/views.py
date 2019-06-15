from datetime import datetime, timedelta
from .models import BaseInfo as User
from .models import SmsCode
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework import status
from django.db.models import Q
from .serializers import UserSerializer, SmsCodeSerializer
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils import http as utils_http
from utils import string as utils_string
from utils import sms as utils_sms

class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = SmsCodeSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证合法
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        template = serializer.validated_data["template"]
        success, res = utils_sms.send_ramdom_code(mobile, template)
        if success:
            db_model = SmsCode(code=res, mobile=mobile)
            db_model.save()
            return utils_http.gen_success_response()
        else:
            return utils_http.gen_error_response(res)

class UserViewSet(viewsets.ViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = UserSerializer

    @list_route(methods=['GET'],
    authentication_classes=[JSONWebTokenAuthentication],
    permission_classes=[permissions.IsAuthenticated],
    url_path="test")
    def test(self, request, *args, **kwargs):
        user = request.user
        return Response(data={"test": "test-----1213", 'user': user.username})


class AccountViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer

    @list_route(methods=['POST'],
    permission_classes=[permissions.AllowAny])
    def login(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        users = User.objects.filter(username__exact=username) or User.objects.filter(mobile__exact=username)
        if users and len(users) > 0:
            user = users[0]
            if user.check_password(password):
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response("Success! Token is " + token, status=status.HTTP_200_OK)
            else:
                return Response("Password Error!!", status=status.HTTP_400_BAD_REQUEST)
        return Response("User doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    def register(self):
        return Response(data={"register": "register-----1213"})

    def change_password(self):
        pass

    def change_name(self):
        pass
