from django.test import TestCase
from LittleLemonAPI.models import MenuItem
class MenuTest(TestCase):
    def test_post_item(self):
        item = MenuItem.objects.create(title='IceCream', price=80, inventory = 100)
        self.assertEqual(str(item), "IceCream : 80")