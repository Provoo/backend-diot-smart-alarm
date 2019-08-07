from rest_framework import status, generics, request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

from django.contrib.auth.models import User


import requests

from .serializers import CreateUserSerializer, MomBabySerializer, MomToolsSerializer, MomUserSerializer, BabyToolsSerializer, UserImagesSerializer
from .models import MomUser, MomBabies, MomTools, BabyTools, UserImages

CLIENT_ID = '<client-id>'
CLIENT_SECRET = '<client-secret>'


class UserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class MomUserDataView(generics.CreateAPIView):
    queryset = MomUser.objects.select_related('momId')
    lookup_field = "momId"
    serializer_class = MomUserSerializer


class MomUserDetailsView(generics.RetrieveUpdateAPIView):
    queryset = MomUser.objects.select_related('momId')
    lookup_field = "momId"
    serializer_class = MomUserSerializer


class MomBabiesView(generics.CreateAPIView):
    queryset = MomBabies.objects.select_related('momId')
    permission_classes = [AllowAny]
    serializer_class = MomBabySerializer


class MomBabiesList(generics.ListAPIView):
    queryset = MomBabies.objects.select_related('momId')
    permission_classes = [AllowAny]
    serializer_class = MomBabySerializer

    def get_queryset(self):
        momData = MomBabies.objects.filter(
            momId=self.kwargs['momId'])
        return momData


class MomBabiesDetailView(generics.RetrieveUpdateAPIView):
    queryset = MomBabies.objects.select_related('momId')
    serializer_class = MomBabySerializer


class MomToolsView(generics.CreateAPIView):
    model = MomTools
    serializer_class = MomToolsSerializer

class MomToolsDetailView(generics.RetrieveUpdateAPIView):
    queryset = MomTools.objects.select_related('momId')
    serializer_class = MomToolsSerializer


class BabyToolsView(generics.CreateAPIView):
    model = BabyTools
    serializer_class = BabyToolsSerializer


class BabyToolsDetailView(generics.RetrieveUpdateAPIView):
    queryset = BabyTools.objects.select_related('babyId')
    serializer_class = BabyToolsSerializer


class UserImagesView(generics.CreateAPIView):
    model = UserImages
    serializer_class = UserImagesSerializer

