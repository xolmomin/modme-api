from rest_framework.serializers import ModelSerializer

from users.models import Company, Branch, Role


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ()

class BranchModelSerializer(ModelSerializer):
    class Meta:
        model = Branch
        exclude = ()


class RoleModelSerializer(ModelSerializer):
    class Meta:
        model = Role
        exclude = ()
