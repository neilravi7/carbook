from django.urls import path
from . import views

# AUTHENTICATION VIEWS
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'account'

urlpatterns=[
    path('auth/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create.json', views.UserProfileAPI.as_view(), name='user_create'),
]
