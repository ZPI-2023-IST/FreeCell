class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.color = suit in ['h', 'd']

        self.rank_to_value = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }

    def is_smaller_and_different_color(self, other: object) -> bool:
        return self.rank == other.rank- 1  and self.color != other.color

    def is_larger_and_same_suit(self, other: object) -> bool:
        return self.rank == other.rank + 1 and self.suit == other.suit

    def __le__(self, other):
        return self.rank <= other.rank and self.suit == other.suit

    def __eq__(self, other):

        if other is None:
            return False

        return self.rank == other.rank and self.suit == other.suit

    def __repr__(self):
        if self.rank in self.rank_to_value:
            return f'{self.rank_to_value[self.rank]} of {self.suit}'
        return f'{self.rank} of {self.suit}'

    def __str__(self) -> str:
        if self.rank in self.rank_to_value:
            return f'{self.rank_to_value[self.rank]} + {self.suit}'
        else:
            return f'{self.rank} + {self.suit}'
