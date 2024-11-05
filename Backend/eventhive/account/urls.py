from django.urls import path, include
from .views import UserRegistrationView, UserLoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh view
]
