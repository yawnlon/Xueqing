from datetime import datetime, timedelta
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import SmsCode
from utils import string as utils_string
from utils import http as utils_http
from utils import sms as utils_sms
User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'mobile', 'type')

class MobileSerializer(serializers.Serializer):
    '''
    需要验证手机号的序列器
    '''
    mobile = serializers.CharField(max_length = 11, required=True, allow_blank=False)
    
    def validate_mobile(self, mobile):
        if not utils_string.check_mobile_valid(mobile, utils_string.MOBILE_TYPE_HOME):
            raise utils_http.APIException400("您请求的手机号码非法")
        return mobile

class SmsCodeSerializer(MobileSerializer):
    '''
    短信验证码
    '''
    check_mobile_exist = serializers.BooleanField(default=True)      
    
    def validate(self, attrs):
        check_exist = attrs["check_mobile_exist"]
        mobile = attrs["mobile"]
        exist = User.objects.filter(mobile=mobile).count() > 0
        if check_exist and not exist: # 手机号必须存在在数据库中，例如登录、修改密码、身份验证等
            raise utils_http.APIException400("您请求的手机号尚未注册")
        elif not check_exist and exist: # 手机号必须不存在在数据库中，例如注册等
            raise utils_http.APIException400("您请求的手机号已经注册")
        return attrs
    
class SmsSendSerializer(SmsCodeSerializer):
    '''
    短信验证码发送
    '''
    template = serializers.CharField(max_length = 20, default=utils_sms.SMS_TEPLATE_CODE_USER_AUTH)
    
    def validate_template(self, template):
        if not template in utils_sms.SMS_TEPLATE_CODE_SET:
            raise utils_http.APIException400("您请求的短信模板不合法")
        return template
    
    def validate_mobile(self, mobile):
        super().validate_mobile(mobile)
        # 验证码发送频率
        # 60s内只能发送一次
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if SmsCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise utils_http.APIException400("距离上一次短信发送未超过60s")
        return mobile

class SmsVerifySerializer(SmsCodeSerializer):
    '''
    短信验证码验证，目前这个接口不会让验证码失效
    '''
    code = serializers.CharField(min_length=utils_sms.SMS_RANDOM_CODE_LENGTH,
        max_length=utils_sms.SMS_RANDOM_CODE_LENGTH, label="验证码", required=True)

    def validate(self, attrs):
        super().validate(attrs)
        mobile = attrs["mobile"]
        code = attrs["code"]
        success, msg = utils_sms.verify_random_code(mobile, code, invalid=False)
        if not success:
            raise utils_http.APIException400(msg)
        return attrs

class SelfSerializer(serializers.Serializer):
    def get_user(self):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            return user
        else:
            raise utils_http.APIException400("未知错误")

class SelfVerifySerializer(SelfSerializer):
    '''
    验证当前登录用户的密码和验证码是否准确
    ''' 

    password = serializers.CharField(
        style={'input_type': 'password'}, label=True, write_only=True, default=None
    )

    code = serializers.CharField(min_length=utils_sms.SMS_RANDOM_CODE_LENGTH,
        max_length=utils_sms.SMS_RANDOM_CODE_LENGTH, label="验证码", required=True)

    def validate_code(self, code):
        user = self.get_user()
        success, msg = utils_sms.verify_random_code(user.mobile, code)
        if not success:
            raise utils_http.APIException400(msg)
        return code

    def validate_password(self, password):
        user = self.get_user()
        if not user.check_password(password):
            raise utils_http.APIException400("您输入的密码错误")


class UserLoginSerializer(MobileSerializer):
    '''
    用户登录
    ''' 
    password = serializers.CharField(
        style={'input_type': 'password'}, label=True, write_only=True, default=None
    )   
    code = serializers.CharField(min_length=utils_sms.SMS_RANDOM_CODE_LENGTH,
        max_length=utils_sms.SMS_RANDOM_CODE_LENGTH, label="验证码", default=None)

    def validate_mobile(self, mobile):
        super().validate_mobile(mobile)
        if not User.objects.filter(mobile__exact=mobile).count():
            raise utils_http.APIException400("您请求的手机号码尚未注册")
        return mobile
        
    def validate(self, attrs):
        mobile = attrs["mobile"]
        password = attrs["password"]
        code = attrs["code"]
        user = User.objects.get(mobile=mobile)
        if not (password or code):
            raise utils_http.APIException400("请输入密码或手机验证码登录")
        if password:
            if not user.check_password(password):
                raise utils_http.APIException400("您输入的密码错误")
        elif code:
            success, msg = utils_sms.verify_random_code(mobile, code)
            if not success:
                raise utils_http.APIException400(msg)
        return attrs

class UserVerifySerializer(SmsVerifySerializer):

    '''
    用户忘记密码或注册，用于验证code和密码是否合法
    密码是新设的密码
    '''

    password = serializers.CharField(
        style={'input_type': 'password'}, label=True, write_only=True, required=True
    )

    def validate_password(self, password):
        valid, msg = utils_string.check_password_valid(password)
        if not valid:
            raise utils_http.APIException400(msg)
        return password

class UserRegisterSerializer(UserVerifySerializer):
    '''
    用户注册
    '''
    name = serializers.CharField(max_length=50, default="学清用户", label="用户名")
    check_mobile_exist = serializers.BooleanField(default=False)    

class UserChangeMobileSerializer(UserVerifySerializer):
    '''
    用户修改手机号
    密码是用户的密码
    '''
    check_mobile_exist = serializers.BooleanField(default=False)

    def validate_password(self, password):
        super().validate_password(password)
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if not user.check_password(password):
                raise utils_http.APIException400("您输入的密码错误")
        return password

class UserChangePasswordSerializer(SmsVerifySerializer):
    password_old = serializers.CharField(
        style={'input_type': 'password'}, label=True, write_only=True, required=True
    )

    password_new = serializers.CharField(
        style={'input_type': 'password'}, label=True, write_only=True, required=True
    )

    def validate_mobile(self, mobile):
        super().validate_mobile(mobile)
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user.mobile != mobile:
                raise utils_http.APIException400("您输入的手机号不是当前账号")
        else:
            raise utils_http.APIException400("未知错误")
        return mobile


    def validate_password_old(self, password_old):
        valid, msg = utils_string.check_password_valid(password_old)
        if not valid:
            raise utils_http.APIException400(msg)
        return password_old

    def validate_password_new(self, password_new):
        valid, msg = utils_string.check_password_valid(password_new)
        if not valid:
            raise utils_http.APIException400(msg)
        return password_new

    def validate(self, attrs):
        mobile = attrs["mobile"]
        password_old = attrs["password_old"]
        user = User.objects.get(mobile=mobile)
        if not user.check_password(password_old):
            raise utils_http.APIException400("您输入的旧密码错误")
        super().validate(attrs)
        return attrs  

class UserChangeNameSerializer(serializers.Serializer):
    '''
    用户修改姓名
    '''
    name = serializers.CharField(max_length=50, required=True, label="用户名")

