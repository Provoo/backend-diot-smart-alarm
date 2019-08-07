from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class DiodDiveceType(models.Model):
    code = models.StrignField(unique=True, primary_key=True)
    userId = models.OneToOneField(
        User)
    code = models.OneToOneField(
        DiodDiveceType)

        
class DiotDivice(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    userId = models.OneToOneField(
        User)
    code = models.OneToOneField(
        DiodDiveceType)
    

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