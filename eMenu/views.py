from django.shortcuts import render
from django.views import generic
from eMenu.models import Card


class CardsListView(generic.ListView):
    model = Card
    template_name = 'all_cards_table.html'
    context_object_name = 'all_cards_list'
    paginate_by = 5
    queryset = Card.objects.exclude(dish=None)


class CardDetailView(generic.DetailView):
    model = Card
    template_name = 'card_detail.html'
    context_object_name = 'card'
