from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils import timezone

import uuid


class DiodDiveceTypes(models.Model):
    code = models.CharField(unique=True, max_length=30, primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    date_of_launch = models.DateTimeField(default=timezone.now)
    version = models.CharField(max_length=5)

class DiotDivice(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    userId = models.OneToOneField(
        User, on_delete=models.CASCADE)
    code = models.OneToOneField(
        DiodDiveceTypes, on_delete=models.CASCADE)
    

class Dh11Sensor(models.Model):
    ditoDiviceId =  models.OneToOneField(
        DiotDivice, on_delete=models.CASCADE, primary_key=True)
    states = JSONField(default=list)

class Mq2Sensor(models.Model):
    ditoDiviceId =  models.OneToOneField(
        DiotDivice, on_delete=models.CASCADE, primary_key=True)
    states = JSONField(default=list)

class MagnetiqSensor(models.Model):
    ditoDiviceId =  models.OneToOneField(
        DiotDivice, on_delete=models.CASCADE, primary_key=True)
    states = JSONField(default=list)
