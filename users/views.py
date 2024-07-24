from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializers import UserSerializer


class RegisterUserView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
