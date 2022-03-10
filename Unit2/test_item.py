import unittest
from item import *
import numpy as np

class TestItem(unittest.TestCase):
    def setUp(self):
        self.item1 = Item('guitar','Gibson Les Paul Standard',np.float64(500.00) ,'10001a',np.int64(5),'abc')
        self.item2 = Item('bass','Ibanez Acoustic Electric',np.float64(300.10) ,'10100a', np.int64(2),'abc')
    def test00_init(self):
        # make sure that everything was correct
        self.assertEqual(self.item1.get_name(), 'Gibson Les Paul Standard')
        self.assertEqual(self.item1.get_price(), 500.00)

    def test01_update_stock(self):
        self.item1.update_stock(2)
        self.item2.update_stock(-1)
        self.assertEqual(self.item1.get_stock(), 7)
        self.assertEqual(self.item2.get_stock(), 1)
        self.assertRaises(TypeError, self.item2.update_stock, "string")

    def test03_set_price(self):
        self.assertRaises(TypeError, self.item2.set_price, "string")
        self.item2.set_price(np.float64(200))
        self.assertEqual(self.item2.get_price(), 200)