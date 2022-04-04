import unittest
from model import can_add

class Test_Check_Add(unittest.TestCase):
    def setUp(self):
       pass
    def test_success(self):
        # check to make sure it can be added to an empty cart
        self.assertTrue(can_add({},'emp101001'))
        # check to make sure that quantity can be updated
        self.assertTrue(can_add({'emp101001': 1},'emp101001'))
        # check to make sure a different item can be added
        self.assertTrue(can_add({},'a5gf3po'))
        # check to make it can be added to a cart with multiple items
        self.assertTrue(can_add({'emp101001': 1, 'a5gf3po': 2},'a5gf3po'))
    def test_fail(self):
        # make sure we can't add a model number that isn't in inventory
        self.assertFalse(can_add({}, 'not a valid model'))
        # make sure we can't add more than the stock store has
        self.assertFalse(can_add({'emp101001': 13}, 'emp101001'))