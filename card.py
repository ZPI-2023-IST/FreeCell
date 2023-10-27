class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.color = suit in ['h', 'd']

    def is_smaller_and_different_color(self, other: object) -> bool:
        pass

    def is_larger_and_same_suit(self, other: object) -> bool:
        pass

    def __repr__(self):
        return f'{self.rank} of {self.suit}'
    
    def __str__(self) -> str:
        return {self.rank} + {self.suit}