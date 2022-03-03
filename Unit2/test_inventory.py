#Hiram will test Andres' inventory file
import unittest
import inventory

class TestInventory(unittest.TestCase):

    #update_quantity
    def test_update_quantity(self):
        self.assertRaises(ValueError, inventory.update_quantity, 'axe', 1)
    
    #change_price
    def test_change_price(self):
        self.assertRaises(ValueError, inventory.change_price, 'axe', 1)

    #check_inventory
    def test_check_inventory(self):
        self.assertRaises(ValueError, inventory.check_inventory, 'axe', 1)

    #return_instrument_dic
    def test_return_instrument_dic(self):
        self.assertRaises(ValueError, inventory.return_instrument, 'axe', 1)
