# from rest_framework import serializers
# from utils import webhook as utils_webhook
# from utils import http as utils_http

# class WebhookSerializer(serializers.Serializer):
#     password = serializers.CharField(required=True, allow_blank=False)
#     # hook_name = serializers.CharField(required=True, allow_blank=False)

#     def validate_password(self, password):
#         if password != utils_webhook.PASSWORD:
#             raise utils_http.APIException400("密码错误")
#         return password
    