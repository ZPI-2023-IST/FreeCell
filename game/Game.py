from enum import Enum


class State(Enum):
    ONGOING = 0
    WON = 1
    LOST = 2


class Game:
    def get_moves(self) -> list:
        pass

    def make_move(self, move: tuple) -> bool:
        pass

    def get_state(self) -> State:
        pass

    def get_board(self) -> list:
        pass
