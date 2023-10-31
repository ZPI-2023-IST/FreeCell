from unittest import TestCase
from Board import Board
from unittest.mock import Mock
from Card import Card


class TestBoard(TestCase):

    def create_mock_card(self):
        card = Mock(spec=Card)
        return card

    def test_empty_cells_all_board_empty(self):
        empty_deck = []
        board = Board(empty_deck)
        self.assertEquals(board.empty_cells(),4+8)

    def test_empty_cells_and_move_to_free_cell_real_moves(self):
        empty_deck = []
        board = Board(empty_deck)
        mocked_cards = [self.create_mock_card() for _ in range(3)]

        board.move_to_free_cell(mocked_cards[0])
        board.move_to_free_cell(mocked_cards[1])

        board.move_to_free_column(mocked_cards[2])

        self.assertEqual(board.empty_cells(), 4 - 2 + 8 - 1)
        self.assertEqual(board.columns[0], [mocked_cards[2]])
        self.assertEqual(board.free_cells, [mocked_cards[0],mocked_cards[1],None,None])

    def test_make_deck(self):
        cards = [self.create_mock_card() for _ in range(52)]
        board = Board(cards)

        expected_columns = [
            cards[0:6], cards[6:12], cards[12:18], cards[18:24],
            cards[24:31], cards[31:38], cards[38:45], cards[45:52]
        ]

        self.assertEqual(board.columns, expected_columns)

    def test_move_to_stack(self):
        cardAh = Card(1, 'h')
        cardAs = Card(1, 's')
        cardAd = Card(1, 'd')
        cardAc = Card(1, 'c')

        board = Board([cardAh,cardAs,cardAd,cardAc])

        self.assertTrue(board.move_to_stack(cardAh))
        self.assertTrue(board.move_to_stack(cardAc))
        self.assertTrue(board.move_to_stack(cardAs))
        self.assertTrue(board.move_to_stack(cardAd))

        self.assertTrue(board.suit_stack['h'] is cardAh)
        self.assertTrue(board.suit_stack['d'] is cardAd)
        self.assertTrue(board.suit_stack['s'] is cardAs)
        self.assertTrue(board.suit_stack['c'] is cardAc)

        card2h = Card(2, 'h')

        self.assertTrue(board.move_to_stack(card2h))
        self.assertTrue(board.suit_stack['h'] is card2h)

    def test_move_to_card_single_card_move(self):
        card3h = Card(3, 'h')
        card2s = Card(2, 's')
        card4d = Card(4, 'd')
        card5s = Card(5, 's')

        board = Board([])
        board.columns[0] = [card5s]
        board.columns[2] = [card2s]
        board.columns[3] = [card4d]
        board.columns[4] = [card3h]

        self.assertTrue(board.move_to_card(card2s, card3h))
        self.assertTrue(board.columns[4] == [card3h,card2s])



    def test_move_to_card_multiple_card_move_good_order(self):
        card3h = Card(3, 'h')
        card2s = Card(2, 's')
        card4s = Card(4, 's')
        card5d = Card(5, 'd')

        board = Board([])
        board.columns[0] = [card5d]
        board.columns[2] = [card2s]
        board.columns[3] = [card4s]
        board.columns[4] = [card3h]

        self.assertTrue(board.move_to_card(card2s, card3h))
        self.assertTrue(board.columns[4] == [card3h,card2s])
        self.assertTrue(board.move_to_card(card3h, card4s))
        self.assertTrue(board.columns[3] == [card4s,card3h,card2s])


