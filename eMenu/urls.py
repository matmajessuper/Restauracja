from django.urls import path

from . import views

urlpatterns = [
    path('', views.CardsListView.as_view(), name='all_cards_list'),
    path('<int:pk>', views.CardDetailView.as_view(), name='card_detail'),
]