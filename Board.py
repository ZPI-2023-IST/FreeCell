from Card import Card


class Board:
    def __init__(self, cards: list) -> None:
        self.columns = []
        self.free_cells = [None for _ in range(4)]
        self.suit_stack = {'h': None, 'd': None, 'c': None, 's': None}
        self.__make_deck(cards)

    def __make_deck(self, cards: list) -> None:
        start = 0
        cards_per_column = [6] * 4 + [7] * 4

        for num_cards in cards_per_column:
            column = cards[start:start + num_cards]
            self.columns.append(column)
            start += num_cards

    def empty_cells(self) -> int:
        return self.free_cells.count(None) + self.columns.count([])
    
    def get_movable_cards(self) -> list:
        """Get all cards from the top of columns.
        
        :return: A list of all cards that may be moved.
        """
        movable_cards = []
        for column in self.columns:
            if column:
                movable_cards.append(column[-1])
        return movable_cards

    def move_to_stack(self, card: Card) -> bool:
        col = self.__is_on_top(card)

        if not col:
            return False

        if card.is_larger_and_same_suit(self.suit_stack[card.suit]):
            self.suit_stack[card.suit] = card
            col.pop()
            return True

        return False

    def move_to_free_cell(self, card: Card) -> bool:

        col = self.__is_on_top(card)

        if not col:
            return False

        if self.free_cells.count(None) > 0:
            for i in range(len(self.free_cells)):
                if self.free_cells[i] is None:
                    self.free_cells[i] = card
                    col.pop()
                    return True

    def __is_on_top(self, card: Card) -> list:
        col = next((col for col in self.columns if card in col), None)

        if card == col[-1]:
            return col

        return []

    def move_to_free_column(self, card: Card) -> bool:

        # check if there is any free column
        if self.columns.count([]) < 1:
            return False

        if card in self.free_cells:
            return self.__move_card_from_free_cell_to_empty_column(card)

        source_column = next((col for col in self.columns if card in col), None)
        if source_column:
            cards_to_move = source_column[source_column.index(card):]

            valid_sequence = all(
                card.is_smaller_and_different_color(prev_card)
                for card, prev_card in zip(cards_to_move[1:], cards_to_move)
            )

            if len(cards_to_move) <= self.empty_cells() and valid_sequence:
                self.columns[next(i for i, col in enumerate(self.columns) if not col)].extend(cards_to_move)

                index_of_card_to_move = source_column.index(card)
                source_column[index_of_card_to_move:] = source_column[:index_of_card_to_move]

                return True  # Move successful

        return False  # Move unsuccessful

    def __move_card_from_free_cell_to_card(self, card_to_move: Card, destination_card: Card) -> bool:
        self.columns[next(i for i, col in enumerate(self.columns) if destination_card in col)].append(card_to_move)
        self.free_cells[self.free_cells.index(card_to_move)] = None
        return True

    def __move_card_from_free_cell_to_empty_column(self, card_to_move: Card) -> bool:
        self.columns[next(i for i, col in enumerate(self.columns) if not col)].append(card_to_move)
        self.free_cells[self.free_cells.index(card_to_move)] = None
        return True

    def move_to_card(self, card_to_move: Card, destination_card: Card) -> bool:

        if card_to_move.is_smaller_and_different_color(destination_card):

            # Check if card is in free cell
            if card_to_move in self.free_cells:
                return self.__move_card_from_free_cell_to_card(card_to_move, destination_card)

            dest_column = self.__is_on_top(destination_card)
            source_column = self.__is_on_top(card_to_move)

            if dest_column and source_column:
                # Determine the cards to move
                cards_to_move = source_column[source_column.index(card_to_move):]

                # Check if there are enough empty cells
                if len(cards_to_move) <= self.empty_cells():
                    # Move the cards
                    dest_column.extend(cards_to_move)
                    index_of_card_to_move = source_column.index(card_to_move)
                    source_column[index_of_card_to_move:] = source_column[:index_of_card_to_move]

                    return True  # Move successful

        return False
