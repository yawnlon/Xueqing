from datetime import datetime, timedelta
from .models import BaseInfo as User
from .models import SmsCode
from .models import StudentInfo
from rest_framework import viewsets, mixins
from rest_framework import permissions
from rest_framework import status
from django.db.models import Q
from .serializers import UserSerializer, UserLoginSerializer
from .serializers import UserRegisterSerializer, UserVerifySerializer
from .serializers import SmsSendSerializer, SmsVerifySerializer
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_encode_handler,jwt_payload_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils import http as utils_http
from utils import string as utils_string
from utils import sms as utils_sms
from django.utils import timezone

class SmsCodeViewSet(viewsets.GenericViewSet):
    # serializer_class = SmsCodeSerializer
    permission_classes = [permissions.AllowAny]

    @list_route(methods=['POST'],
    serializer_class=SmsSendSerializer)
    def send(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证合法
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        template = serializer.validated_data["template"]
        success, res = utils_sms.send_ramdom_code(mobile, template)
        # success, res = True, "989899"
        if success:
            if SmsCode.objects.filter(mobile=mobile).count():
                model = SmsCode.objects.get(mobile=mobile)
                model.code = res
                model.save()
            else:
                model = SmsCode(code=res, mobile=mobile)
                model.save()
            return utils_http.gen_success_response("发送成功")
        else:
            return utils_http.gen_error_response(res)

    @list_route(methods=['POST'],
    serializer_class=SmsVerifySerializer)
    def verify(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证合法
        serializer.is_valid(raise_exception=True)
        return utils_http.gen_success_response("验证成功")

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
        return Response(data={"test": "test-----1213", 
            'user': {
                 "id": user.id,
                "username": user.username,
                "mobile": user.mobile,
                "type": user.get_type_display(),
                "is_active": user.is_active
            }})

class AccountViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer

    @list_route(methods=['POST'],
    serializer_class = UserLoginSerializer,
    permission_classes=[permissions.AllowAny])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        user = User.objects.get(mobile=mobile)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        return utils_http.gen_success_response("登录成功", {
            "user": {
                "id": user.id,
                "username": user.username,
                "mobile": user.mobile,
                "type": user.get_type_display(),
                "is_active": user.is_active
            },
            "token": token,
        })
    
    @list_route(methods=['POST'],
    serializer_class = UserRegisterSerializer,
    permission_classes=[permissions.AllowAny])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        password = serializer.validated_data["password"]
        name = serializer.validated_data["name"]
        user = User(mobile=mobile, 
            username="xq_" + mobile,
            password=password,
            last_login=timezone.now())
        user.set_password(password)
        user.save()
        student = StudentInfo.objects.create(user=user, name=name)
        payload = jwt_payload_handler(student.user)
        token = jwt_encode_handler(payload)
        return utils_http.gen_success_response("注册成功", {
            "user": {
                "id": user.id,
                "username": user.username,
                "mobile": user.mobile,
                "type": user.get_type_display(),
                "is_active": user.is_active,
                "name": student.name
            },
            "token": token
        })

    @list_route(methods=['POST'],
    serializer_class = UserVerifySerializer,
    permission_classes=[permissions.AllowAny],
    url_path="reset-password")
    def reset_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        password = serializer.validated_data["password"]
        user = User.objects.get(mobile=mobile)
        user.set_password(password)
        user.save()
        return utils_http.gen_success_response("密码修改成功，请重新登录")

    def change_name(self):
        pass
