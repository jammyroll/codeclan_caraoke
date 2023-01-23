import unittest
from classes.Guest import Guest
from classes.Room import Room
from classes.Song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.Guest = Guest('Jim',50,"Don't fear the reaper")

    def test_guest_has_name(self):
        self.assertEqual('Jim',self.Guest.name)
   
    def test_guest_has_money(self):
        self.assertEqual(50,self.Guest.wallet)


