from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json, random
from users.models import SmsCode
from datetime import datetime, timedelta

ACCESSKEY_ID = "LTAIcVDWhhluB0vg"
ACCESSKEY_SECRET = "Zf2l7WRYUMCaEpeIGiFwsH5KbikUuv"
REGION_ID = "default"

SMS_SIGN_NAME = "好学知"
SMS_TEPLATE_CODE_USER_AUTH = "SMS_167655084" #身份验证
SMS_TEPLATE_CODE_LOGIN_AUTH = "SMS_167655083" #登录验证
SMS_TEPLATE_CODE_LOGIN_EXCEPTION = "SMS_167655082" #登录异常
SMS_TEPLATE_CODE_USER_REGISTER = "SMS_167655081" #用户注册
SMS_TEPLATE_CODE_CHANGE_PASSWORD = "SMS_167655080" #修改密码

SMS_TEPLATE_CODE_SET = set()
SMS_TEPLATE_CODE_SET.add(SMS_TEPLATE_CODE_USER_AUTH)
SMS_TEPLATE_CODE_SET.add(SMS_TEPLATE_CODE_LOGIN_AUTH)
SMS_TEPLATE_CODE_SET.add(SMS_TEPLATE_CODE_LOGIN_EXCEPTION)
SMS_TEPLATE_CODE_SET.add(SMS_TEPLATE_CODE_USER_REGISTER)
SMS_TEPLATE_CODE_SET.add(SMS_TEPLATE_CODE_CHANGE_PASSWORD)


SMS_RANDOM_CODE_SEEDS = "0123456789"
SMS_RANDOM_CODE_LENGTH = 6
SMS_RANDOM_CODE_EXPIRED_TIME = 5 * 60 # 单位 sec

SMS_RESPONSE_CODE_SUCCESS = "OK"
SMS_RESPONSE_CODE_FAIL = {
    'isv.OUT_OF_SERVICE': '服务端短信业务余额不足导致业务停机',
    'isv.DAY_LIMIT_CONTROL': '已经达到您在控制台设置的短信日发送量限额值',
    'isv.INVALID_PARAMETERS': '参数格式不正确',
    'isp.SYSTEM_ERROR': '系统错误',
    'isv.MOBILE_NUMBER_ILLEGAL': '手机号码格式错误',
    'isv.BUSINESS_LIMIT_CONTROL': '短信发送频率超限',
    'isv.AMOUNT_NOT_ENOUGH': '当前账户余额不足',
    'isv.SMS_TEMPLATE_ILLEGAL': '短信模板不存在，或未经审核通过'
}

def send_ramdom_code(mobile, template):
    return AliyunSMS().send_random_code(mobile, template)

def verify_random_code(mobile, code, invalid=True):
    try:
        last = SmsCode.objects.get(mobile=mobile)
        if datetime.now() > last.add_time + timedelta(seconds=SMS_RANDOM_CODE_EXPIRED_TIME):
            return False, "验证码已经过期"
        if last.code != code:
            return False, "验证码错误"
        if last.used:
            return False, "验证码失效"
        if invalid:
            last.used = True
            last.save()
        return True, None
    except SmsCode.DoesNotExist:
        return False, "验证码不存在，请发送手机验证码"


class AliyunSMS(object):

    def __init__(self):
        self.client = AcsClient(ACCESSKEY_ID, ACCESSKEY_SECRET, REGION_ID)

    def init_sendsms_request(self):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https') # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')
        return request
    
    def gen_random_code(self):
        result = []
        for _ in range(SMS_RANDOM_CODE_LENGTH):
            result.append(random.choice(SMS_RANDOM_CODE_SEEDS))
        return "".join(result)

    def send_random_code(self, mobile, template):
        request = self.init_sendsms_request()
        request.add_query_param('PhoneNumbers', mobile)
        request.add_query_param('SignName', SMS_SIGN_NAME)
        request.add_query_param('TemplateCode', template)
        sms_code = self.gen_random_code()
        param =  "{\"code\": \"" + sms_code + "\"}"
        request.add_query_param('TemplateParam', param)
        response = self.client.do_action(request)
        res = json.loads(str(response, encoding = 'utf-8'))
        # print(res)
        code = res["Code"]
        if code == SMS_RESPONSE_CODE_SUCCESS:
            return True, sms_code
        elif code in SMS_RESPONSE_CODE_FAIL.keys():
            return False, SMS_RESPONSE_CODE_FAIL[code]
        else:
            return False, res["Message"]

