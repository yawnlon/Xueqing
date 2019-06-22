from django.shortcuts import render
from rest_framework import viewsets
from .models import StudyCard
from .serializers import StudyCardSerializer

# Create your views here.

class StudyCardViewSet(viewsets.ModelViewSet):
    queryset = StudyCard.objects.all()
    serializer_class = StudyCardSerializer
    # permission_classes = 