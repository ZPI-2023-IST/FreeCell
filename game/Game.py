from enum import Enum
from abc import ABC, abstractmethod


class State(Enum):
    ONGOING = 0
    WON = 1
    LOST = 2


class Game(ABC):
    @abstractmethod
    def get_moves(self) -> list:
        pass

    @abstractmethod
    def make_move(self, move: tuple) -> bool:
        pass

    @abstractmethod
    def get_state(self) -> State:
        pass

    @abstractmethod
    def get_board(self) -> list:
        pass

    @abstractmethod
    def start_game(self) -> None:
        pass
