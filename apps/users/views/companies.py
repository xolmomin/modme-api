from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from users.filters import CompanyFilter
from users.models import Company, Branch, Course
from users.serializers.companies import CompanyModelSerializer, BranchModelSerializer, CreateCompanyModelSerializer, \
    UpdateCompanyModelSerializer, PartialUpdateCompanyModelSerializer


class CompanyModelViewSet(ModelViewSet):
    queryset = Company.objects.order_by('id')
    serializer_class = CompanyModelSerializer
    filterset_fields = ['name']
    ordering_fields = ['name', 'id', 'created_at']
    search_fields = ['name', 'start_of_working_day', 'id']
    # filterset_fields = {
    #     'name': ['icontains'],
        # 'date': ['gte']
    # }
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = CompanyFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return CreateCompanyModelSerializer
        # elif self.action == 'create':
        #     return
        # elif self.action == 'retrieve':
        #     return
        elif self.action == 'update':
            return UpdateCompanyModelSerializer
        elif self.action == 'partial_update':
            return PartialUpdateCompanyModelSerializer
        # elif self.action == 'destroy':
        #     return

        return super().get_serializer_class()


class BranchModelViewSet(ModelViewSet):
    queryset = Branch.objects.order_by('id')
    serializer_class = BranchModelSerializer
    filterset_fields = ['company', 'name']

    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return CreateCompanyModelSerializer
    #     elif self.action == 'list':
    #         return ListCompanyModelSerializer
    #     return super().get_serializer_class()
    #
    # @action
    # def
