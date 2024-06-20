from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from auth_jwt.views import RegistrationAPIView, UserAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('user/', UserAPIView.as_view()),
    path('user/<int:user_id>/', UserAPIView.as_view()),
]