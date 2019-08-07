from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
#  \ from .views import getBdPToken, getBdPAcoounts, getBdPBalance, getTransactions, generateOtp, validateOtp, transferToAccount, blockAccount
from .views import MomUserDataView, MomUserDetailsView, MomBabiesView, \
    MomBabiesDetailView, MomToolsView, MomToolsDetailView, \
    MomBabiesList, UserView, BabyToolsView, BabyToolsDetailView, UserImagesView


urlpatterns = [
    path('user_info/<int:pk>/', UserView.as_view()),
    path('info_user/', MomUserDataView.as_view()),
    path('info_user/<int:momId>/', MomUserDetailsView.as_view()),
    path('create_mom_baby/', MomBabiesView.as_view()),
    path('list_mom_baby/<int:momId>/', MomBabiesList.as_view()),
    path('mom_baby/<int:pk>/', MomBabiesDetailView.as_view()),
    path('create_mom_tools/', MomToolsView.as_view()),
    path('get_mom_tools/<int:pk>/', MomToolsDetailView.as_view()),
    path('create_baby_tools/', BabyToolsView.as_view()),
    path('get_baby_tools/<int:pk>/', BabyToolsDetailView.as_view()),
    path('upload_image/', UserImagesView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
