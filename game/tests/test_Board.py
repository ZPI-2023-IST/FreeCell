from unittest import TestCase
from game.Board import Board
from unittest.mock import Mock
from game.Card import Card


class TestBoard(TestCase):
    def create_mock_card(self):
        card = Mock(spec=Card)
        return card

    def test_empty_cells_all_board_empty(self):
        empty_deck = []
        board = Board(empty_deck)
        self.assertEqual(board.empty_cells(), 4 + 8)

    def test_empty_cells_and_move_to_free_cell_real_moves(self):
        empty_deck = []
        board = Board(empty_deck)
        card3h = Card(3, "h")
        card2s = Card(2, "s")
        card4s = Card(4, "s")
        card5d = Card(5, "d")
        card1h = Card(1, "h")

        board.columns[0] = [card5d]
        board.columns[2] = [card2s, card1h]
        board.columns[3] = [card4s]
        board.columns[4] = [card3h]

        self.assertEqual(board.empty_cells(), 4 + 8 - 4)

        self.assertTrue(board.move_to_free_cell(card1h))
        self.assertEqual(board.empty_cells(), 4 - 1 + 8 - 4)

        self.assertTrue(board.move_to_free_cell(card2s))
        self.assertEqual(board.empty_cells(), 4 - 2 + 8 - 3)

        self.assertEqual(board.columns[2], [])
        self.assertEqual(board.free_cells, [card1h, card2s, None, None])

    def test_make_deck(self):
        cards = [self.create_mock_card() for _ in range(52)]
        board = Board(cards)

        expected_columns = [
            cards[0:6],
            cards[6:12],
            cards[12:18],
            cards[18:24],
            cards[24:31],
            cards[31:38],
            cards[38:45],
            cards[45:52],
        ]

        self.assertEqual(board.columns, expected_columns)

    def test_move_to_stack_only_aces(self):
        cardAh = Card(1, "h")
        cardAs = Card(1, "s")
        cardAd = Card(1, "d")
        cardAc = Card(1, "c")

        board = Board([cardAh, cardAs, cardAd, cardAc])

        self.assertTrue(board.move_to_stack(cardAc))
        self.assertTrue(board.move_to_stack(cardAd))
        self.assertTrue(board.move_to_stack(cardAs))
        self.assertTrue(board.move_to_stack(cardAh))

        self.assertTrue(board.suit_stack["h"] is cardAh)
        self.assertTrue(board.suit_stack["d"] is cardAd)
        self.assertTrue(board.suit_stack["s"] is cardAs)
        self.assertTrue(board.suit_stack["c"] is cardAc)

    def test_move_to_stack_aces_then_2_and_3(self):
        cardAh = Card(1, "h")
        cardAs = Card(1, "s")
        cardAd = Card(1, "d")
        cardAc = Card(1, "c")
        card2h = Card(2, "h")
        card3h = Card(3, "h")

        board = Board([])

        board.columns[0] = [cardAh, cardAs, cardAd, cardAc]
        board.columns[1] = [card2h]
        board.columns[2] = [card3h]

        self.assertTrue(board.move_to_stack(cardAc))
        self.assertTrue(board.move_to_stack(cardAd))
        self.assertTrue(board.move_to_stack(cardAs))
        self.assertTrue(board.move_to_stack(cardAh))

        self.assertTrue(board.suit_stack["h"] is cardAh)
        self.assertTrue(board.suit_stack["d"] is cardAd)
        self.assertTrue(board.suit_stack["s"] is cardAs)
        self.assertTrue(board.suit_stack["c"] is cardAc)

        self.assertTrue(board.move_to_stack(card2h))
        self.assertTrue(board.suit_stack["h"] is card2h)

        self.assertTrue(board.move_to_stack(card3h))
        self.assertTrue(board.suit_stack["h"] is card3h)

    def test_move_to_card_single_card_move(self):
        card3h = Card(3, "h")
        card2s = Card(2, "s")
        card4d = Card(4, "d")
        card5s = Card(5, "s")

        board = Board([])
        board.columns[0] = [card5s]
        board.columns[2] = [card2s]
        board.columns[3] = [card4d]
        board.columns[4] = [card3h]

        self.assertTrue(board.move_to_card(card2s, card3h))
        self.assertTrue(board.columns[4] == [card3h, card2s])

    def test_move_to_free_column(self):
        card3h = Card(3, "h")  # 3 of Hearts
        card2s = Card(2, "s")  # 2 of Spades
        card3d = Card(3, "d")  # 3 of Diamonds
        card4s = Card(4, "s")  # 4 of Spades
        card5d = Card(5, "d")  # 5 of Diamonds
        card8c = Card(8, "c")  # 8 of Clubs
        card6h = Card(6, "h")  # 6 of Hearts
        card9s = Card(9, "s")  # 9 of Spades
        card8d = Card(8, "d")  # 8 of Diamonds
        card10h = Card(10, "h")  # 10 of Hearts
        card2c = Card(2, "c")  # 2 of Clubs
        card5s = Card(5, "s")  # 5 of Spades
        card7d = Card(7, "d")  # 7 of Diamonds
        card6c = Card(6, "c")  # 6 of Clubs

        cards = [
            [card3h, card2s, card3d, card4s, card5d, card8c],
            [card6h, card9s, card8d, card10h, card2c, card5s],
            [card7d, card6c],
            [],
            [],
            [],
            [],
            [],
        ]
        board = Board([])
        board.columns = cards

        # [
        # [3 of h, 2 of s, 3 of d, 4 of s, 5 of d, 8 of c],
        # [6 of h, 9 of s, 8 of d, 10 of h, 2 of c, 5 of s],
        # [7 of d, 6 of c],
        # [],
        # [],
        # [],
        # [],
        # []
        # ]

        self.assertTrue(board.move_to_free_column(card6c))
        # [
        # [3 of h, 2 of s, 3 of d, 4 of s, 5 of d, 8 of c],
        # [6 of h, 9 of s, 8 of d, 10 of h, 2 of c, 5 of s],
        # [7 of d],
        # [6 of c],
        # [],
        # [],
        # [],
        # []
        # ]
        self.assertEqual(board.columns[3], [card6c])
        self.assertEqual(board.columns[2], [card7d])

        self.assertFalse(board.move_to_free_column(card5d))

    def test_move_card_from_free_cell_to_card(self):
        card3h = Card(3, "h")  # 3 of Hearts
        card2s = Card(2, "s")  # 2 of Spades
        card3d = Card(3, "d")  # 3 of Diamonds
        card4s = Card(4, "s")  # 4 of Spades
        card5d = Card(5, "d")  # 5 of Diamonds
        card8c = Card(8, "c")  # 8 of Clubs
        card6h = Card(6, "h")  # 6 of Hearts
        card9s = Card(9, "s")  # 9 of Spades
        card8d = Card(8, "d")  # 8 of Diamonds
        card10h = Card(10, "h")  # 10 of Hearts
        card2c = Card(2, "c")  # 2 of Clubs
        card5s = Card(5, "s")  # 5 of Spades
        card7d = Card(7, "d")  # 7 of Diamonds
        card6c = Card(6, "c")  # 6 of Clubs

        cards = [
            [card3h, card2s, card3d, card4s, card5d, card8c],
            [card6h, card9s, card8d, card10h, card2c, card5s],
            [card7d, card6c],
            [],
            [],
            [],
            [],
            [],
        ]
        board = Board([])
        board.columns = cards

        # [
        # [3 of h, 2 of s, 3 of d, 4 of s, 5 of d, 8 of c],
        # [6 of h, 9 of s, 8 of d, 10 of h, 2 of c, 5 of s],
        # [7 of d, 6 of c],
        # [],
        # [],
        # [],
        # [],
        # []
        # ]
        self.assertTrue(board.move_to_free_cell(card6c))
        self.assertEqual(board.free_cells[0], card6c)
        self.assertTrue(board.move_to_card(card6c, card7d))
        self.assertTrue(board.columns[2] == [card7d, card6c])

    def test_move_card_from_free_cell_to_column(self):
        card3h = Card(3, "h")  # 3 of Hearts
        card2s = Card(2, "s")  # 2 of Spades
        card3d = Card(3, "d")  # 3 of Diamonds
        card4s = Card(4, "s")  # 4 of Spades
        card5d = Card(5, "d")  # 5 of Diamonds
        card8c = Card(8, "c")  # 8 of Clubs
        card6h = Card(6, "h")  # 6 of Hearts
        card9s = Card(9, "s")  # 9 of Spades
        card8d = Card(8, "d")  # 8 of Diamonds
        card10h = Card(10, "h")  # 10 of Hearts
        card2c = Card(2, "c")  # 2 of Clubs
        card5s = Card(5, "s")  # 5 of Spades
        card7d = Card(7, "d")  # 7 of Diamonds
        card6c = Card(6, "c")  # 6 of Clubs

        cards = [
            [card3h, card2s, card3d, card4s, card5d, card8c],
            [card6h, card9s, card8d, card10h, card2c, card5s],
            [card7d, card6c],
            [],
            [],
            [],
            [],
            [],
        ]
        board = Board([])
        board.columns = cards

        # [
        # [3 of h, 2 of s, 3 of d, 4 of s, 5 of d, 8 of c],
        # [6 of h, 9 of s, 8 of d, 10 of h, 2 of c, 5 of s],
        # [7 of d, 6 of c],
        # [],
        # [],
        # [],
        # [],
        # []
        # ]

        self.assertTrue(board.move_to_free_cell(card6c))
        self.assertEqual(board.free_cells[0], card6c)
        self.assertTrue(board.move_to_free_column(card6c))
        self.assertTrue(board.columns[3] == [card6c])
        self.assertTrue(board.free_cells[0] is None)
