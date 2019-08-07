from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField, JSONField


# Create your models here.


class MomUser(models.Model):
    momId = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    profileImage = models.ImageField(blank=True)


babySexChoices = (
    ('M','Male'), 
    ('F','Female'),
    ('N', 'NA')
    )

class MomBabies(models.Model):
    momId = models.ForeignKey(User, on_delete=models.CASCADE)
    babyName = models.CharField(max_length=100, blank=True)
    babySex = models.CharField(max_length=1, choices=babySexChoices)
    pregnacyDay = models.DateField(null=True, blank=True)
    babyBrithDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.babyName


class MomTools(models.Model):
    momId = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    babyNames = JSONField(default=list)
    simpleList = JSONField(default=list)
    diary = JSONField(default=list)
    calendar = JSONField(default=list)


class BabyTools(models.Model):
    babyId = models.OneToOneField(
        MomBabies, on_delete=models.CASCADE, primary_key=True)
    vaccines = JSONField(default=list)
    babyDiary = JSONField(default=list)
    babyData = JSONField(default=list)

class UserImages(models.Model):
    momId = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

   
    
#Todo Decir el calendario
