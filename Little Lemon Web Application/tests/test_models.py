#
# python .\manage.py test
#
# __init__.py MUST exist else the test won't run!
#

from django.test import TestCase

from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        the_string = str(item)
        self.assertEqual(the_string, "IceCream : 80")
