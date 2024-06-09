from django.test import TestCase
from .models import Menu

class TestMenu(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(tittle='IceCream', price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")