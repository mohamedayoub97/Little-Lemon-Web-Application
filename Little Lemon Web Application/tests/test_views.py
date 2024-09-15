#
# python .\manage.py test
#
# __init__.py MUST exist else the test won't run!
#

from django.test import TestCase
from django.urls import resolve, reverse

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from restaurant.views import MenuItemsView

from random import randint


MENU_ITEMS = {
    1: {'title': 'ApplePie',     'price': 13.78, 'inventory': randint(1, 10)},
    2: {'title': 'VanillaLatte', 'price': 3.99,  'inventory': randint(1, 10)},
    3: {'title': 'Icecream',     'price': 5.00,  'inventory': randint(1, 10)},
    4: {'title': 'IrishCoffe',   'price': 7.89,  'inventory': randint(1, 10)},
}

class MenuViewTest(TestCase):
    items = MENU_ITEMS

    def setUp(self) -> None:
        # Create menu items
        for i in self.items.keys():
            item = Menu.objects.create(
                title = self.items[i]['title'],
                price = self.items[i]['price'],
                inventory = self.items[i]['inventory'],
            )
            item.save()  #TODO: Why?

        return super().setUp()

    def test_getall(self):
        # Does 'menu-items' connect to MenuItemsView?
        url = reverse('menu-items')
        self.assertEqual(resolve(url).func.view_class, MenuItemsView)

        response = self.client.get(reverse('menu-items'))
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        self.assertEqual(response.status_code, 200)
#       self.assertEqual(response.data, serializer.data)
