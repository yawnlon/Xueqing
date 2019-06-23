from rest_framework import serializers
from .models import StudyCard
from utils import string as utils_string
from utils import http as utils_http

class StudyCardSerializer(serializers.ModelSerializer):

    def validate_code(self, code):
        if not utils_string.check_pure_letter_valid(code):
            raise utils_http.APIException400("您请求的学习卡代号格式非法")
        return code

    def validate(self, attrs):
        class_free = attrs["class_free"]
        class_general = attrs["class_general"]
        class_vip = attrs["class_vip"]
        if not class_free and not class_general and not class_vip:
            raise utils_http.APIException400("必须选择一种课程类型")
        return attrs

    class Meta:
        model = StudyCard
        # fields = ('name', 'code', 'introduction', 'class_free', 'class_general', 'class_vip')
        fields = "__all__"