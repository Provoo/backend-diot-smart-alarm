from django.contrib import admin

from .models import (DiotDiveceTypes,
                     DiotDivice)


@admin.register(DiotDivice)
class DiotDiviceAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'userId',
                    'code',
                    'publish_topics',
                    'subcribers_topics')


@admin.register(DiotDiveceTypes)
class DiotDiveceTypesAdmin(admin.ModelAdmin):
    list_display = ('code',
                    'name',
                    'date_of_launch',
                    'version',
                    'publish_chanels',
                    'subcribers_chanels',
                    )
