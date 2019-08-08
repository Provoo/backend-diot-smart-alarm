from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Dh11SensorView


urlpatterns = [
    path('temperature/<str:ditoDiviceId>/', Dh11SensorView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
