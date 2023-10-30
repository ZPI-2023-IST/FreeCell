from Game import Game
from Board import Board
from Deck import Deck

class FreeCell(Game):
    def __init__(self):
        self._move_count = 0
        self.deck = Deck()
        self.board = Board(self.deck.cards_shuffled())

    def increment_move_count(self):
        self._move_count += 1

    # Overridden functions from Game class

    def get_all_moves(self) -> list:
        pass

    def make_move(self, move: tuple) -> None:
        pass

    def get_state(self) -> list:
        pass

    def get_board(self) -> list:
        pass