from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import MomUser, MomBabies, MomTools, BabyTools, UserImages



@receiver(post_save, sender=User)
def mom_tools_handler(sender, instance, created, **kwargs):
    if created:
        userImage = MomUser(momId=instance)
        userImage.save()
        momtools = MomTools(momId=instance)
        momtools.save()


@receiver(post_save, sender=MomBabies)
def baby_tools_handler(sender, instance, created, **kwargs):
    if created:
        userImage = BabyTools(babyId=instance)
        userImage.save()


