from rest_framework.serializers import ModelSerializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'branch', 'phone', 'gender', 'date_of_birth', 'balance', 'photo', 'addition_contact', 'datas')
