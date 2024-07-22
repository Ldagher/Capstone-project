# test_views.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer  # Replace with the actual import if necessary

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name="Breakfast Special", price=5.99, description="A special breakfast menu item")
        self.menu2 = Menu.objects.create(name="Lunch Special", price=10.99, description="A special lunch menu item")
        self.menu3 = Menu.objects.create(name="Dinner Special", price=15.99, description="A special dinner menu item")

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))  # Adjust the URL name to match your URL pattern name
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
