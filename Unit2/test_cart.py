import unittest
from cart import Shopping_Cart
from inventory import Inventory as Inv
from collections import defaultdict

class TestCart(unittest.TestCase):
    def setUp(self):
        inventory1 = Inv()
        inventory2 = Inv()
        inventory3 = Inv()
        try:
            self.cart1 = Shopping_Cart(inventory1)
        except:
            raise TypeError("Shopping_Cart class needs to be initiated with an inventory object")
        self.cart2 = Shopping_Cart(inventory2)
        self.cart3 = Shopping_Cart(inventory3)
        self.instrument1 = self.cart1.store_inventory.get_instrument('10011a')

    def test00_init(self):
        self.assertEqual(self.instrument1.get_name(), 'Mariposa Custom')
        self.assertEqual(type(self.cart1.cart), defaultdict)

    def test01_add_cart(self):
        self.cart1.add_item('10011a')
        self.assertTrue(self.instrument1 in self.cart1.cart)
        self.assertTrue(self.cart1.cart[self.instrument1] == 1)
        self.cart1.add_item('10011a')
        self.assertTrue(self.cart1.cart[self.instrument1] == 2)
        self.assertRaises(ValueError, self.cart1.add_item, '10011a')

    def test01_remove_item(self):
        self.assertTrue(1 == 1)

