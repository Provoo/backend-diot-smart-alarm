from django.contrib import admin

from .models import (Dh11Sensor, DiodDiveceTypes,
                     DiotDivice, Mq2Sensor)
# Register your models here.
@admin.register(Dh11Sensor)
class Dh11SensorAdmin(admin.ModelAdmin):
    display_list = ('ditoDiviceId',
                    'states',)


@admin.register(DiodDiveceTypes)
class DiodDiveceTypesAdmin(admin.ModelAdmin):
    display_list = ('code',
                    'name',
                    'date_of_launch',
                    'version',)


@admin.register(DiotDivice)
class DiodDiveceAdmin(admin.ModelAdmin):
    display_list = ('id',
                    'userId',
                    'code',)
