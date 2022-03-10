import imp
import unittest
from src.bear import Bear
from src.river import River

class TestBear(unittest.TestCase):
    def setUp(self):
        self.bear_1 = Bear("Berry", ["salmon"])

    def test_has_name(self):
        self.assertEqual("Berry", self.bear_1.bear_name)

    def test_has_stomach(self):
        self.assertEqual(["salmon"] , self.bear_1.stomach)

    def test_take_fish(self):
        river = River(["fish_1", "fish_2", "fish_3"])
        self.bear_1.take_fish_from_river(river.fish_stock, "fish_1")
        self.assertEqual(["fish_2", "fish_3"], river.fish_stock)
        self.assertEqual(["salmon", "fish_1"], self.bear_1.stomach)

    def test_count_fish_in_stomach(self):
        number_of_elements = self.bear_1.count_fish_in_stomach()
        self.assertEqual(1, number_of_elements)

    def test_sleep_bear(self):
        self.assertEqual([], self.bear_1.sleep_bear())



