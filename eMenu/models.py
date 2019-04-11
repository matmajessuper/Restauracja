from django.db import models


class Dish(models.Model):
    img = models.ImageField(verbose_name='Image', upload_to='dishes/', null=True, blank=True)
    name = models.CharField(verbose_name='Name', max_length=50)
    description = models.TextField(verbose_name='Description')
    price = models.IntegerField(verbose_name='Price')
    preparation_time = models.CharField(verbose_name='Preparation time', max_length=15)
    date_added = models.DateTimeField(verbose_name='Date added', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    vegetarian = models.BooleanField(verbose_name='Vegetarian dish')

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(verbose_name='Name', max_length=20, unique=True)
    description = models.TextField(verbose_name='Description')
    date_added = models.DateTimeField(verbose_name='Date added', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    dish = models.ManyToManyField(Dish, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

    @property
    def number(self):
        return self.dish.count()
