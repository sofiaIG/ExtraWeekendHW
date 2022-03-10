import unittest
from src.river import*
from src.fish import*

class TestRiver(unittest.TestCase):
    def setUp(self):
        self.river = River(["salmon", "cod", "some other fish"])

    def test_has_stock(self):
        self.assertEqual(["salmon", "cod", "some other fish"], self.river.fish_stock)

    def test_add_fish_to_river(self):
        self.assertEqual(["salmon", "cod", "some other fish", "fish"], self.river.add_fish_to_river("fish"))
