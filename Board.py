from Card import Card

class Board:
    def __init__(self, cards: list()) -> None:
        self.columns = cards
        self.free_cells = list()
        self.suit_stack = {'h': None, 'd': None, 'c': None, 's': None}

    def empty_cells(self) -> int:
        pass

    def move_to_free_cell(self, card: Card) -> None:
        pass

    def move_to_card(self, card: Card, Card: int) -> None:
        pass