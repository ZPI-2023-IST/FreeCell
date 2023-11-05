class Card:
    """
        Represents a playing card with a rank, suit, and color.

        Args:
            rank (int): The rank of the card.
            suit (str): The suit of the card ('h' for hearts, 'd' for diamonds, 'c' for clubs, 's' for spades).

        Attributes:
            rank (int): The rank of the card.
            suit (str): The suit of the card.
            color (bool): True if the card's suit is red (hearts or diamonds), False otherwise.

        Methods:
            is_smaller_and_different_color(self, other: Card) -> bool:
                Checks if the card is one rank smaller and of a different color than another card.

            is_larger_and_same_suit(self, other: Card) -> bool:
                Checks if the card is one rank larger and of the same suit as another card.

        Special Methods:
            __le__(self, other: Card) -> bool:
                Compares the card with another card based on rank and suit.

            __eq__(self, other: object) -> bool:
                Checks if the card is equal to another card or None.

            __repr__(self) -> str:
                Returns a string representation of the card.

            __str__(self) -> str:
                Returns a string representation of the card.

        """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.color = suit in ['h', 'd']

        self.rank_to_value = {
            1: 'A',
            10: 'T',
            11: 'J',
            12: 'Q',
            13: 'K'
        }

    def is_smaller_and_different_color(self, other: object) -> bool:
        """Checks if the card is one rank smaller and of a different color than another card.

        Args:
            other (object): Another card to compare to.

        Returns:
            bool: True if the conditions are met, False otherwise.
        """
        
        return self.rank == other.rank - 1  and self.color != other.color

    def is_larger_and_same_suit(self, other: object) -> bool:        
        """
        Checks if the card is one rank larger and of the same suit as another card.

        Args:
            other (object): Another card to compare to.

        Returns:
            bool: True if the conditions are met, False otherwise.
        """
        
        if other is None:
            return self.rank == 1
        return self.rank == other.rank + 1 and self.suit == other.suit

    def __le__(self, other):
        return self.rank <= other.rank and self.suit == other.suit

    def __eq__(self, other):

        if other is None:
            return False

        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        if self.rank in self.rank_to_value:
            return f'{self.rank_to_value[self.rank]} of {self.suit}'
        return f'{self.rank} of {self.suit}'

    def __repr__(self) -> str:
        if self.rank in self.rank_to_value:
            return f'{self.rank_to_value[self.rank]}{self.suit}'
        else:
            return f'{self.rank}{self.suit}'
