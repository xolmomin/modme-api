from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from users.models import Company, Branch, Role


class CompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        exclude = ()


class CreateCompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'start_of_working_day', 'end_of_working_day')
        read_only_fields = ('start_of_working_day', 'end_of_working_day')
        # write_only_fields = ('start_of_working_day', )
        # extra_kwargs = {
        # }


class UpdateCompanyModelSerializer(ModelSerializer):
    class Meta:
        model = Company
        # fields = ('id', 'name', 'start_of_working_day', 'end_of_working_day')
        exclude = ('deleted_at', 'is_deleted')
        # read_only_fields = ('start_of_working_day', 'end_of_working_day')
        # write_only_fields = ('start_of_working_day', )
        # extra_kwargs = {
        # }


class PartialUpdateCompanyModelSerializer(ModelSerializer):
    name = CharField(max_length=255, required=False)

    class Meta:
        model = Company
        # fields = ('id', 'name', 'start_of_working_day', 'end_of_working_day')
        exclude = ('deleted_at', 'is_deleted')
        # read_only_fields = ('start_of_working_day', 'end_of_working_day')
        # write_only_fields = ('start_of_working_day', )
        # extra_kwargs = {
        # }


class BranchModelSerializer(ModelSerializer):
    class Meta:
        model = Branch
        exclude = ()


class RoleModelSerializer(ModelSerializer):
    class Meta:
        model = Role
        exclude = ()
