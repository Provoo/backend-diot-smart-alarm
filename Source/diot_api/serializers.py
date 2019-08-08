from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Dh11Sensor


class Dh11SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dh11Sensor
        fields = '__all__'
