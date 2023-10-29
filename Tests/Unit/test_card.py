from unittest import TestCase
from Freecell.Card import Card

class TestCard(TestCase):

    def setUp(self):
        # Color 1
        self.card4h = Card(4, 'h')
        self.card2h = Card(2, 'h')
        self.card5d = Card(5, 'd')

        # Color 2
        self.card10s = Card(10, 's')
        self.card7s = Card(7, 's')
        self.card2c = Card(2, 'c')

    def test_is_smaller_and_different_color(self):
        self.assertTrue(self.card2h.is_smaller_and_different_color(self.card10s))
        self.assertTrue(self.card5d.is_smaller_and_different_color(self.card7s))

        self.assertFalse(self.card2h.is_smaller_and_different_color(self.card2c))
        self.assertFalse(self.card2h.is_smaller_and_different_color(self.card4h))

    def test_is_larger_and_same_suit(self):
        self.assertTrue(self.card4h.is_larger_and_same_suit(self.card2h))
        self.assertTrue(self.card10s.is_larger_and_same_suit(self.card7s))

        self.assertFalse(self.card2h.is_larger_and_same_suit(self.card5d))
        self.assertFalse(self.card2h.is_larger_and_same_suit(self.card7s))
