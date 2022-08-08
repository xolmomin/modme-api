from rest_framework.serializers import ModelSerializer

from users.models import Company, Branch, Role


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company


class BranchModelSerializer(ModelSerializer):
    class Meta:
        model = Branch


class RoleModelSerializer(ModelSerializer):
    class Meta:
        model = Role
