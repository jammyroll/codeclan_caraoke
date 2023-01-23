import unittest
from classes.Guest import *
from classes.Room import *
from classes.Song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room('Rock Room',100)
        self.guest = Guest('Jim',50,"Don't feat the reaper")
        self.song = Song('Blue Oyster Cult', "Don't fear the reaper")
        self.guest1 = Guest('Jimmy',51,"Don't fear the reaper")
        self.guest2 = Guest('Jimithy',52,"Don't fear the reaper")
        self.guest3 = Guest('Jimbob',53,"Don't fear the reaper")
        self.guest4 = Guest('Jimeroni',54,"Highway to Hell")



    def test_room_has_name(self):

        expected = 'Rock Room'
        tested = self.room.name
        self.assertEqual(expected,tested)

    def test_room_has_till(self):
        self.assertEqual(100,self.room.till)

    def test_can_add_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual('Jim',self.room.singers[0].name)


    def test_can_remove_guest(self):
        self.room.add_guest(self.guest)
        self.room.remove_guest(self.guest)
        self.assertEqual(0,len(self.room.singers))
        

    def test_can_add_song_to_room(self):
        self.room.add_song_to_room(self.song)
        self.assertEqual("Blue Oyster Cult",self.room.song_list[0].artist)

    
    def test_check_if_there_is_space_in_room(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.room.add_guest(self.guest3)
        self.assertEqual('Sorry the room is full, try another',self.room.add_guest(self.guest4))

    def test_check_money_is_removed_from_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(45,self.room.singers[0].wallet)
        self.assertEqual(105,self.room.till)

    def test_check_if_favorite_song_is_available(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest3)
        self.assertEqual('Jimmy yells Woo', self.room.add_song_to_room(self.song))

        


