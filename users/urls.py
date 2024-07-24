from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import RegisterUserView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
]