from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Dish(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    description = models.TextField(verbose_name=_('Description'))
    price = models.IntegerField(verbose_name=_('Price'))
    preparation_time = models.CharField(verbose_name=_('Preparation time'), max_length=15)
    date_added = models.DateTimeField(verbose_name=_('Date added'), auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_('Date updated'), auto_now=True)
    vegetarian = models.BooleanField(verbose_name=_('Vegetarian dish'))

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=20, unique=True)
    description = models.TextField(verbose_name=_('Description'))
    date_added = models.DateTimeField(verbose_name=_('Date added'), auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_('Date updated'), auto_now=True)
    dish = models.ManyToManyField(Dish, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
