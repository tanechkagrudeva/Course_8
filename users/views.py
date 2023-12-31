from rest_framework.generics import CreateAPIView, ListAPIView

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    API view for create a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    """
    API view for display the list of all users.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
