from django.db.models import Count
from django.db.models.functions import Length
from django_filters import NumberFilter, CharFilter, FilterSet, ChoiceFilter
from django_filters.filters import Filter

from users.models import Company, User


class CompanyFilter(FilterSet):
    # min_price = NumberFilter(field_name="price", lookup_expr='gte')
    # max_price = NumberFilter(field_name="price", lookup_expr='lte')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    n = NumberFilter(field_name='name', method='filter_by_name_len')

    def filter_by_name_len(self, queryset, name, value):
        queryset = queryset.annotate(name_ledsabdjnsan=Length('name'))
        return queryset.filter(name_len__gte=value)

    class Meta:
        model = Company
        # exclude = ()
        fields = ['name']
        # fields = {
        #     'name': ['contains']
        # }


class UserFilter(FilterSet):
    type = ChoiceFilter(field_name='user_type', choices=User.Type.choices)

    class Meta:
        model = User
        fields = ['gender']

