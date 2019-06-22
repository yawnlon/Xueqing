from rest_framework import serializers

class QiniuSaveSerializer(serializers.Serializer):
    key = serializers.CharField(max_length = 500, required=True, allow_blank=False)