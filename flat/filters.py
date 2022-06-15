import django_filters
from . import models
class FlatFilter(django_filters.FilterSet):
    class Meta:
        model = models.Flat
        fields=['Район','Комнат','Цена','Сотрудники']