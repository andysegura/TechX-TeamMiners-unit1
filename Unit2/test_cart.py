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
            self.cart1 = Shopping_Cart(inventory1) #test00, test01
        except:
            raise TypeError("Shopping_Cart class needs to be initiated with an inventory object")
        self.cart2 = Shopping_Cart(inventory2) #test02
        self.cart3 = Shopping_Cart(inventory3) #test03
        self.instrument1 = self.cart1.store_inventory.get_instrument('10011a') #mariposa custom, test00, test01
        self.instrument2 = self.cart2.store_inventory.get_instrument('10001a') #gibson standard, test02
        self.instrument3 = self.cart3.store_inventory.get_instrument('11000a') #Sunn Solarus 250.99, test03
        self.instrument4 = self.cart3.store_inventory.get_instrument('11001a') #Empress Delay 220.33, test03


    def test00_init(self):
        #making sure inventory class is working correctly inside cart
        self.assertEqual(self.instrument1.get_name(), 'Mariposa Custom')
        #making sure types are the same
        self.assertEqual(type(self.cart1.cart), defaultdict)

    def test01_add_cart(self):
        self.cart1.add_item('10011a')
        #making sure instrument is in cart
        self.assertTrue(self.instrument1 in self.cart1.cart)
        #making sure count in shopping cart is accurate
        self.assertTrue(self.cart1.cart[self.instrument1] == 1)
        self.cart1.add_item('10011a')
        #making sure count in shopping cart is accurate
        self.assertTrue(self.cart1.cart[self.instrument1] == 2)
        #making sure an exception is raised when trying to add an item that is not in stock
        self.assertRaises(ValueError, self.cart1.add_item, '10011a')

    def test02_remove_item(self):
        self.cart2.add_item('10001a')
        self.cart2.remove_item('10001a')
        #making sure the item is not in the cart
        self.assertTrue(self.instrument2 not in self.cart2.cart)
        #making sure an exception gets raised when trying to remove item from cart
        self.assertRaises(ValueError, self.cart2.remove_item, '10011a')

    def test03_checkout(self):
        model1 = self.instrument3.model_number
        model2 = self.instrument4.model_number
        self.cart3.add_item(model1) #250.99
        self.cart3.add_item(model2) #220.33
        self.cart3.add_item(model2) #220.33 expected balance = 691.95
        self.assertAlmostEqual(self.cart3.cart_total, 691.65)
        self.assertTrue(self.cart3.checkout(691.65)) #checkout transaction completed succesfully
        self.assertRaises(ValueError, self.cart3.checkout, 59.99) #payment too low
        self.assertRaises(ValueError, self.cart3.checkout, 899.99) #payment too high