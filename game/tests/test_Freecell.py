from unittest import TestCase
from game.Freecell import FreeCell
from game.Game import State
from game.Card import Card


class TestFreecell(TestCase):
    def __flatten_list(self, _list: list) -> list:
        return [elem for sublist in _list for elem in sublist]

    def setup_scenario_various_moves(self) -> FreeCell:
        return FreeCell()

    def setup_scenario_stack_move(self) -> FreeCell:
        freecell = FreeCell()
        freecell.board.columns = [
            [Card(13, "h")],
            [Card(13, "d")],
            [Card(13, "s")],
            [Card(13, "c")],
            [Card(4, "h")],
            [Card(4, "d"), Card(2, "c")],
            [Card(4, "s")],
            [Card(4, "c")],
        ]
        freecell.board.free_cells = [
            Card(10, "h"),
            Card(10, "d"),
            Card(10, "s"),
            Card(10, "c"),
        ]
        freecell.board.suit_stack = {
            "h": Card(1, "h"),
            "d": Card(1, "d"),
            "s": Card(1, "s"),
            "c": Card(1, "c"),
        }
        return freecell

    def setup_scenario_free_column(self) -> FreeCell:
        freecell = FreeCell()
        freecell.board.columns = [
            [],
            [Card(13, "d"), Card(7, "c")],
            [Card(13, "s")],
            [Card(13, "c")],
            [Card(3, "h")],
            [Card(3, "d")],
            [Card(3, "s")],
            [Card(3, "c")],
        ]
        freecell.board.free_cells = [
            Card(10, "h"),
            Card(10, "d"),
            Card(10, "s"),
            Card(10, "c"),
        ]
        freecell.board.suit_stack = {
            "h": Card(1, "h"),
            "d": Card(1, "d"),
            "s": Card(1, "s"),
            "c": Card(1, "c"),
        }
        return freecell

    def setup_scenario_empty_board(self) -> FreeCell:
        freecell = FreeCell()
        freecell.board.columns = [[], [], [], [], [], [], [], []]
        freecell.board.free_cells = [None, None, None, None]
        freecell.board.suit_stack = {
            "h": Card(13, "h"),
            "d": Card(13, "d"),
            "s": Card(13, "s"),
            "c": Card(13, "c"),
        }
        return freecell

    def setup_scenario_no_moves(self) -> FreeCell:
        freecell = FreeCell()
        freecell.board.columns = [
            [Card(13, "h")],
            [Card(13, "d")],
            [Card(13, "s")],
            [Card(13, "c")],
            [Card(3, "h")],
            [Card(3, "d")],
            [Card(3, "s")],
            [Card(3, "c")],
        ]
        freecell.board.free_cells = [
            Card(10, "h"),
            Card(10, "d"),
            Card(10, "s"),
            Card(10, "c"),
        ]
        freecell.board.suit_stack = {
            "h": Card(1, "h"),
            "d": Card(1, "d"),
            "s": Card(1, "s"),
            "c": Card(1, "c"),
        }
        return freecell

    def test_scenario_in_progress(self):
        freecell = self.setup_scenario_various_moves()

        columns, free_cells, suit_stack = freecell.get_board()

        assert len(self.__flatten_list(columns))+ len(free_cells) + len(suit_stack) == 60
        assert freecell._move_count == 0

        col1 = freecell.board.columns[0]

        for _ in range(4):
            assert freecell.get_state() == State.ONGOING
            assert freecell.make_move((str(col1[-1]), "F"))

        assert freecell._move_count == 4

    def test_scenario_20_moves(self):
        freecell = self.setup_scenario_various_moves()

        assert freecell.make_move(("Ah", "S"))
        assert freecell.make_move(("9s", "F"))
        assert freecell.make_move(("9d", "F"))
        assert freecell.make_move(("Ad", "S"))
        assert freecell.make_move(("5s", "F"))
        assert freecell.make_move(("Js", "F"))
        assert freecell.make_move(("9d", "Ts"))
        assert freecell.make_move(("6c", "F"))
        assert not freecell.make_move(("Ks", "F"))
        assert freecell.make_move(("5h", "6s"))
        assert freecell.make_move(("9s", "Td"))
        assert freecell.make_move(("4c", "5h"))
        assert not freecell.make_move(("Kc", "S"))
        assert freecell.get_state() == State.ONGOING
        assert freecell.make_move(("7s", "F"))
        assert freecell.make_move(("6c", "7d"))
        assert freecell.make_move(("9s", "F"))
        assert freecell.make_move(("Td", "Jc"))
        assert freecell.make_move(("9s", "Td"))
        assert freecell.make_move(("7s", "8d"))
        assert freecell.make_move(("Kd", "F"))
        assert freecell.make_move(("9c", "F"))
        assert freecell.make_move(("Js", "Qh"))
        assert freecell.make_move(("7s", "F"))
        assert freecell.make_move(("8d", "9s"))
        assert freecell.make_move(("7s", "8d"))
        assert not freecell.make_move(("9s", "Td"))
        assert freecell.make_move(("5c", "F"))
        assert freecell.make_move(("Ac", "S"))
        assert freecell.make_move(("Th", "Js"))
        assert freecell.make_move(("9c", "Th"))
        assert freecell.make_move(("5c", "0"))
        assert freecell.make_move(("7c", "F"))
        assert freecell.make_move(("4d", "F"))
        assert freecell.make_move(("4h", "5c"))
        assert freecell.get_state() == State.ONGOING

    def test_scenario_empty_board(self):
        freecell = self.setup_scenario_empty_board()

        flattened_list = self.__flatten_list(freecell.get_board())
        assert len(flattened_list) == 16

        assert freecell._move_count == 0
        assert not freecell.get_all_moves()
        assert freecell.get_state() == State.WON

    def test_scenario_no_moves(self):
        freecell = self.setup_scenario_no_moves()

        assert freecell._move_count == 0
        assert not freecell.get_all_moves()
        assert freecell.get_state() == State.LOST

    def test_scenario_free_column(self):
        freecell = self.setup_scenario_free_column()
        moves = freecell.get_all_moves()

        assert len(moves) == 11
        assert freecell._move_count == 0
        assert freecell.get_state() == State.ONGOING

        assert freecell.make_move(("7c", "0"))
        assert freecell._move_count == 1
        assert freecell.get_state() == State.LOST

        assert not freecell.make_move(("Kh", "0"))

    def test_scenario_stack_move(self):
        freecell = self.setup_scenario_stack_move()
        moves = freecell.get_all_moves()

        assert len(moves) == 1
        assert freecell._move_count == 0
        assert freecell.get_state() == State.ONGOING

        assert freecell.make_move(("2c", "S"))
        assert freecell._move_count == 1
        assert freecell.get_state() == State.LOST

        assert not freecell.make_move(("Kh", "S"))
