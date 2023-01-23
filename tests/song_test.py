import unittest
from classes.Guest import Guest
from classes.Room import Room
from classes.Song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song('Blue Oyster Cult', "Don't fear the reaper")

    def test_song_has_artist(self):
        self.assertEqual('Blue Oyster Cult',self.song.artist)

    def test_song_has_name(self):
        self.assertEqual("Don't fear the reaper",self.song.song_name)    