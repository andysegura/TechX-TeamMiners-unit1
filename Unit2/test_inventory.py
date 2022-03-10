#Hiram will test Andres' inventory file
import unittest
import inventory
from inventory import Inventory 
from item import *

class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inv1 = Inventory()
        self.model1 = '10010a'
        self.model2 = '11001a'
        self.inst1 = self.inv1.get_instrument(self.model1) #It is the item with name fender stratocaster
        self.inst2 = self.inv1.get_instrument(self.model2) #It is the item with name empress tape delay

    def test00(self):
        self.assertEqual(self.inst1.get_name(), 'Fender Stratocaster')
        self.assertEqual(self.inst2.get_name(), 'empress tape delay')
        self.assertEquals(self.inst1.get_price(), 250.00)
        self.assertEquals(self.inst2.get_price(), 220.33)

    def test01(self):
        self.assertEqual(self.inv1.get_stock(self.model1), self.inst1.get_stock())
        self.assertEqual(self.inv1.get_stock(self.model1), 10)
        self.assertEqual(self.inv1.get_stock(self.model2), self.inst2.get_stock())
        self.assertEqual(self.inv1.get_stock(self.model2), 4)
        
    def test02(self):
        self.inv1.set_stock(self.model1, 11)
        self.assertEqual(self.inv1.get_stock(self.model1), 11)

    def test03(self):
        testInstrument = Item('guitar','Fender Mustang',np.float64(1000.00) ,'101',np.int64(7),'Kurt Cobain Guitar')
        self.inv1.add_instrument(testInstrument)
        testInv = self.inv1.get_instrument('101')
        self.assertEqual(testInstrument,testInv)
