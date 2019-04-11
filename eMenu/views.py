from django.views import generic
from django_tables2 import SingleTableView
from eMenu.models import Card
from eMenu.tables import CardTable


class CardsListView(SingleTableView):
    model = Card
    template_name = 'all_cards_list.html'
    table_data = Card.objects.exclude(dish=None)
    table_class = CardTable
    table_pagination = {
        'per_page': 5
    }


class CardDetailView(generic.DetailView):
    model = Card
    template_name = 'card_detail.html'
    context_object_name = 'card'
