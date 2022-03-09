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
        self.instrument1 = self.cart1.store_inventory.get_instrument('10011a') #mariposa custom
        self.instrument2 = self.cart2.store_inventory.get_instrument('10001a') #gibson standard
        self.instrument3 = self.cart2.store_inventory.get_instrument('10011a') #mariposa custom
        self.instrument4 = self.cart3.store_inventory.get_instrument('11000a') #Sunn Solarus 250.99
        self.instrument5 = self.cart3.store_inventory.get_instrument('11001a') #Empress Delay 220.33


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
        self.cart2.add_item('10001a')
        self.cart2.remove_item('10001a')
        self.assertTrue(self.instrument2 not in self.cart2.cart)
        self.assertRaises(ValueError, self.cart2.remove_item, '10011a')

    def test02_checkout(self):
        model1 = self.instrument4.model_number
        model2 = self.instrument5.model_number
        self.cart3.add_item(model1)
        self.cart3.add_item(model2)
        self.cart3.add_item(model2)
        self.assertAlmostEqual(self.cart3.cart_total, 691.65)
        self.assertTrue(self.cart3.checkout(691.65))
        self.assertRaises(ValueError, self.cart3.checkout, 59.99)
        self.assertRaises(ValueError, self.cart3.checkout, 899.99)