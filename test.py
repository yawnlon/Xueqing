from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json

client = AcsClient('LTAIcVDWhhluB0vg', 'Zf2l7WRYUMCaEpeIGiFwsH5KbikUuv', 'default')

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('dysmsapi.aliyuncs.com')
request.set_method('POST')
request.set_protocol_type('https') # https | http
request.set_version('2017-05-25')
request.set_action_name('SendSms')

request.add_query_param('PhoneNumbers', "18888")
request.add_query_param('SignName', "学清书院")
request.add_query_param('TemplateCode', "SMS_167655083")
request.add_query_param('TemplateParam', "{\"code\": \"2222\"}")

response = client.do_action(request)
# python2:  print(response) 
res = json.loads(str(response, encoding = 'utf-8'))
print(res["Message"])
print(str(response, encoding = 'utf-8'))
