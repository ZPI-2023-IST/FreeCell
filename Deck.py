from typing import Generator

from Card import Card


class Deck:
    def __init__(self, seed: int = 1) -> None:
        self.seed = seed
        self.cards = list()
        for suit in ['h', 'd', 'c', 's']:
            for rank in list(range(1, 14)):
                self.cards.append(Card(rank, suit))

    def __repr__(self) -> str:
        return f'{self.cards}'

    def __str__(self) -> str:
        return f'{self.cards}'

    def _random_generator(self, seed: int) -> Generator[int, None, None]:

        """
        1. The type of values the generator yields (in this case, int).
        2.The type of value that can be sent to the generator with generator.send().
            We are not using send, so we can use None here.
        3. The type of value that the generator returns when it's exhausted or a return statement is encountered.
            In out case, we can use None here as well.
        """

        max_int32 = (1 << 31) - 1
        seed = seed & max_int32

        while True:
            seed = (seed * 214013 + 2531011) & max_int32
            yield seed >> 16

    def cards_shuffled(self) -> list:
        nc = 52
        cards = self.cards.copy()
        rnd = self._random_generator(self.seed)
        for i, r in zip(range(nc), rnd):
            j = (nc - 1) - r % (nc - i)
            cards[i], cards[j] = cards[j], cards[i]
        return cards
