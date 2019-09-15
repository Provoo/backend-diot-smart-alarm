
# Create your views here.
from rest_framework import status, generics, request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

from django.contrib.auth.models import User


from .models import DiotDiveceTypes, DiotDivice

from .serializers import DiotDiveceTypesSerializer, DiotDiviceSerializer


class DiotDiveceTypesView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = DiotDiveceTypes.objects.all()
    serializer_class = DiotDiveceTypesSerializer


class DiotDiviceView(generics.CreateAPIView):
    queryset = DiotDivice.objects.select_related('userId')
    permission_classes = [AllowAny]
    serializer_class = DiotDiviceSerializer


class DiotDiviceDetailView(generics.RetrieveUpdateAPIView):
    queryset = DiotDivice.objects.select_related('userId')
    serializer_class = DiotDiviceSerializer

class DiotDiviceList(generics.ListAPIView):
    queryset = DiotDivice.objects.select_related('userId')
    permission_classes = [AllowAny]
    serializer_class = DiotDiviceSerializer

    def get_queryset(self):
        diotDat = DiotDivice.objects.filter(
            userId=self.kwargs['userId'])
        return diotDat
