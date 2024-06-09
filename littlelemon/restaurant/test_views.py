from django.test import TestCase
from .models import Menu

class TestMenuView(TestCase):
    def setUp(self):
        Menu.objects.create(tittle='Item 1', price=10.00, inventory= 10)
        Menu.objects.create(tittle='Item 2', price=15.00, inventory= 10)
        Menu.objects.create(tittle='Item 3', price=20.00, inventory= 10)
        
    def test_getall(self):
        menus = Menu.objects.all()
        serialized_data = [{'tittle': menu.tittle, 'price': menu.price, 'inventory': menu.inventory} for menu in menus]
        response_data = [{'tittle': 'Item 1', 'price': 10.00, 'inventory': 10},
                         {'tittle': 'Item 2', 'price': 15.00, 'inventory': 10},
                         {'tittle': 'Item 3', 'price': 20.00, 'inventory': 10}]

        self.assertEqual(serialized_data, response_data)