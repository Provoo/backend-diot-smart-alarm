from django.contrib import admin
from .models import MomUser, MomBabies, MomTools, BabyTools, UserImages
# Register your models here.


@admin.register(MomBabies)
class MomBabyAdmin(admin.ModelAdmin):
    list_display = ('momId',
                    'babyName',
                    'babySex',
                    'pregnacyDay',
                    'babyBrithDate')
    # list_filter = ('name')


@admin.register(MomUser)
class MomUserAdmin(admin.ModelAdmin):
    list_display = (
        'momId',
        'profileImage'
    )


@admin.register(MomTools)
class MomToolsAdmin(admin.ModelAdmin):
    list_display = (
        'momId',
        'babyNames',
        'simpleList',
        'diary',
        'calendar'
    )


@admin.register(BabyTools)
class BabyToolsAdmin(admin.ModelAdmin):
    list_display = (
        'babyId',
        'vaccines',
        'babyDiary',
        'babyData'
    )


@admin.register(UserImages)
class UserImagesAdmin(admin.ModelAdmin):
    list_display = (
        'momId',
        'image',
    )
