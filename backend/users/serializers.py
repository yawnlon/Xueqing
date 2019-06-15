from datetime import datetime, timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from utils import string as utils_string
from utils import http as utils_http
from .models import SmsCode
from utils import sms as utils_sms
User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'mobile', 'type')

class SmsCodeSerializer(serializers.Serializer):
    '''
    短信验证码
    '''
    mobile = serializers.CharField(max_length = 11)
    template = serializers.CharField(max_length = 20, default=utils_sms.SMS_TEPLATE_CODE_USER_AUTH)
    check_mobile_exist = serializers.BooleanField(default=True)

    def validate_template(self, template):
        if not template in utils_sms.SMS_TEPLATE_CODE_SET:
            raise utils_http.APIException400("您请求的短信模板不合法")
        return template

    def validate_mobile(self, mobile):
        """
        手机号码验证
        """
        # 是否合法
        if not utils_string.check_mobile_valid(mobile, utils_string.MOBILE_TYPE_HOME):
            raise utils_http.APIException400("您请求的手机号码非法")

        # 验证码发送频率
        # 60s内只能发送一次
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if SmsCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise utils_http.APIException400("距离上一次短信发送未超过60s")

        return mobile
    
    def validate(self, attrs):
        check_exist = attrs["check_mobile_exist"]
        mobile = attrs["mobile"]
        exist = User.objects.filter(mobile=mobile).count() > 0
        if check_exist and not exist: # 手机号必须存在在数据库中，例如登录、修改密码、身份验证等
            raise utils_http.APIException400("您请求的手机号不存在")
        elif not check_exist and exist: # 手机号必须不存在在数据库中，例如注册等
            raise utils_http.APIException400("您请求的手机号已存在")
        return attrs
    
