from rest_framework import serializers
from .models import StudyCard

class StudyCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCard
        fields = ('name', 'code', 'introduction', 'class_free', 'class_general', 'class_vip')