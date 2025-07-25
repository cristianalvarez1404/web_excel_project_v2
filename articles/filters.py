import django_filters
from .models import Article

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    short_desc = django_filters.CharFilter(field_name='short_desc', lookup_expr='icontains')

    class Meta:
        model = Article
        fields = ['title', 'short_desc']
