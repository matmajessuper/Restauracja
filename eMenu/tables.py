import django_tables2 as tables
from django.db.models import F, Count
from django_tables2.utils import A
from .models import Card, Dish


class CardTable(tables.Table):
    id = tables.Column()
    name = tables.LinkColumn('card_detail', args=[A('pk')])
    description = tables.Column(orderable=False)
    date_added = tables.DateTimeColumn(orderable=False)
    date_updated = tables.DateTimeColumn(orderable=False)
    number = tables.Column(verbose_name='Number of dishes')

    class Meta:
        model = Card
        template_name = 'django_tables2/bootstrap.html'
        fields = ['id', 'name', 'description', 'date_added', 'date_updated']

    def render_number(self, record):
        return str(record.dish.count())

    def order_number(self, QuerySet, is_descending):
        QuerySet = QuerySet.annotate(amount=Count('dish')).order_by(('-' if is_descending else '') + 'amount')
        return (QuerySet, True)
