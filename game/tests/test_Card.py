from unittest import TestCase
from game.Card import Card


class TestCard(TestCase):
    def setUp(self):
        # Color 1
        self.card3h = Card(3, "h")
        self.card2h = Card(2, "h")
        self.card5d = Card(5, "d")

        # Color 2
        self.card8s = Card(8, "s")
        self.card7s = Card(7, "s")
        self.card2c = Card(2, "c")
        self.card4c = Card(4, "c")
        self.card3s = Card(3, "s")

    def test_is_smaller_and_different_color(self):
        self.assertTrue(self.card2h.is_smaller_and_different_color(self.card3s))
        self.assertTrue(self.card4c.is_smaller_and_different_color(self.card5d))

        self.assertFalse(self.card2h.is_smaller_and_different_color(self.card2c))
        self.assertFalse(self.card2h.is_smaller_and_different_color(self.card3h))

    def test_is_larger_and_same_suit(self):
        self.assertTrue(self.card3h.is_larger_and_same_suit(self.card2h))
        self.assertTrue(self.card8s.is_larger_and_same_suit(self.card7s))

        self.assertFalse(self.card2h.is_larger_and_same_suit(self.card5d))
        self.assertFalse(self.card2h.is_larger_and_same_suit(self.card7s))

    def test_eq(self):
        card1 = Card(3, "h")
        card2 = Card(3, "h")
        card3 = Card(3, "d")
        card4 = None

        self.assertTrue(
            card1 == card2
        )  # Cards with the same rank and suit should be equal
        self.assertFalse(
            card1 == card3
        )  # Cards with different suits should not be equal
        self.assertFalse(card1 == card4)  # Comparing with None should return False

    def test_repr(self):
        card1 = Card(4, "s")
        card2 = Card(11, "c")

        self.assertEqual(repr(card1), "4 of s")
        self.assertEqual(repr(card2), "J of c")

    def test_str(self):
        card1 = Card(6, "d")
        card2 = Card(10, "h")

        self.assertEqual(str(card1), "6d")
        self.assertEqual(str(card2), "Th")
