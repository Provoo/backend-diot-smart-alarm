from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (DiotDiveceTypesView, DiotDiviceView,
                    DiotDiviceDetailView,DiotDiviceList)


urlpatterns = [
    path('diot_types/', DiotDiveceTypesView.as_view()),
    path('register_diot/', DiotDiviceView.as_view()),
    path('diot_info/<str:pk>', DiotDiviceDetailView.as_view()),
    path('user_diots/<int:userId>', DiotDiviceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
