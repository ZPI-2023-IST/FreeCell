from card import Card

class Deck:
    def __init__(self, seed: int = 1) -> None:
        self.seed = seed
        self.cards = list()
        for suit in ['h', 'd', 'c', 's']:
            for rank in list(range(2, 10)) + ['T', 'J', 'Q', 'K', 'A']:
                self.cards.append(Card(rank, suit))

    def __repr__(self) -> str:
        return f'{self.cards}'
    
    def __str__(self) -> str:
        return f'{self.cards}'
    
    def _random_generator(self, seed: int):
        pass

    def cards_shuffled(self) -> list:
        generator = self._random_generator(self.seed)
        pass