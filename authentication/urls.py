from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='obtain_jwt_token'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='refresh_jwt_token'),
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='verify_jwt_token')
]
