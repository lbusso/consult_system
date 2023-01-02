import django_filters
from django_filters import DateFilter
from .models import *


class ReclamoFilter(django_filters.FilterSet):
    fecha_inicio=DateFilter(field_name='fecha_creada',lookup_expr='gte')
    fecha_fin=DateFilter(field_name='fecha_creada',lookup_expr='lte')
    class Meta:
        model=Reclamo
        fields = '__all__'
