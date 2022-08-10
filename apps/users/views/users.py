from rest_framework.viewsets import ModelViewSet

from users.filters import UserFilter
from users.models import User
from users.serializers.users import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.order_by('id')
    serializer_class = UserModelSerializer
    # filterset_fields = ['name', 'user_type']
    filterset_class = UserFilter
