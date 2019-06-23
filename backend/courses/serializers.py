from rest_framework import serializers
from .models import Course
from utils import http as utils_http

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"