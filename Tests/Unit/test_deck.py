import unittest
from ..Deck import Deck


class TestDeck(unittest.TestCase):
    def test_initialization_default(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)
        self.assertEqual(deck.seed, 1)

    def test_initialization_custom(self):
        custom_seed = 42
        deck = Deck(seed=custom_seed)
        self.assertEqual(deck.seed, custom_seed)
        self.assertEqual(len(deck.cards), 52)

    def test_repr_str(self):
        deck = Deck()
        self.assertEqual(repr(deck), str(deck))

    def test_cards_shuffled(self):
        deck = Deck()
        shuffled_deck = deck.cards_shuffled()

        # Check if the shuffled deck has the same number of cards
        self.assertEqual(len(shuffled_deck), 52)

        # Check if the shuffled deck is not the same as the original deck
        self.assertNotEqual(deck.cards, shuffled_deck)

    def test_custom_seed(self):
        custom_seed = 123
        deck = Deck(seed=custom_seed)
        shuffled_deck = deck.cards_shuffled()

        # Re-create another deck with the same custom seed
        deck2 = Deck(seed=custom_seed)
        shuffled_deck2 = deck2.cards_shuffled()

        # The shuffled decks should be the same because of the same seed
        self.assertEqual(shuffled_deck, shuffled_deck2)
