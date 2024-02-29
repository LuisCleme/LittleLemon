from django.test import TestCase
from LittleLemonAPI.serializers import MenuItemSerializer
from LittleLemonAPI.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        MenuItem.objects.create(title='IceCream', price=100, inventory=10)
        MenuItem.objects.create(title='ArtificialSnow', price=50, inventory=5)
        
    def test_getall(self):
        response = self.client.get('/api/menu-items/')
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, 200)