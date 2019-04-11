from PIL import Image
from django.db import IntegrityError
from django.test import TestCase
from eMenu.models import Card, Dish
from django.core.files.uploadedfile import SimpleUploadedFile


class CardTestCase(TestCase):
    def setUp(self):
        c1 = Card(name='card1')
        c1.save()
        c2 = Card(name='card2')
        c2.save()
        c3 = Card(name='card3')
        c3.save()

    def test_creation_of_common_name_card(self):
        """test card creation with name of existing one"""
        c_common = Card(name='card1')
        with self.assertRaises(IntegrityError):
            c_common.save()

    def test_card_default_ordering(self):
        """test default ordering by id"""
        query = Card.objects.all()
        query_rev = query[::-1]
        self.assertEqual(query[0], Card.objects.get(pk=1))
        self.assertEqual(query_rev[0], Card.objects.get(pk=3))

    def test_nomber_of_dishes(self):
        """test count number of dishes in card"""
        dish1 = Dish(name='dish1', price=1, preparation_time='1min', vegetarian=False)
        dish1.save()
        dish2 = Dish(name='dish2', price=2, preparation_time='1min', vegetarian=False)
        dish2.save()
        dish3 = Dish(name='dish3', price=3, preparation_time='1min', vegetarian=False)
        dish3.save()
        card = Card.objects.all()[0]
        card.dish.add(dish1)
        card.dish.add(dish2)
        card.dish.add(dish3)
        self.assertEqual(3, card.dish.count())


class DishTestCase(TestCase):
    def test_dish_image_adding(self):
        """test image adding"""
        dish = Dish(name='dish1', price='10', preparation_time='10 min', vegetarian=False)
        dish.save()
        self.assertEqual(dish.img, None)
        image_path = 'static/admin/img/Django-Reinhardt.jpg'
        image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        dish.img = image
        dish.save()
        self.assertIsNotNone(dish.img)

