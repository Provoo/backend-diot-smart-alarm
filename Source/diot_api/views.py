
# Create your views here.
from rest_framework import status, generics, request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

from .models import Dh11Sensor
from .serializers import Dh11SensorSerializer


class Dh11SensorView(generics.RetrieveUpdateAPIView):
    permission_classes = []
    queryset = Dh11Sensor.objects.select_related('ditoDiviceId')
    lookup_field = "ditoDiviceId"
    serializer_class = Dh11SensorSerializer
