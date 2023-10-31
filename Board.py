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

    def move_to_stack(self, card: Card) -> bool:

        if self.suit_stack[card.suit] is None and card.rank == 1:
            self.suit_stack[card.suit] = card
            return True
        elif self.suit_stack[card.suit] is not None and card.is_larger_and_same_suit(self.suit_stack[card.suit]):
            self.suit_stack[card.suit] = card
            return True

        return False

    def move_to_free_cell(self, card: Card) -> None:
        if self.free_cells.count(None) > 0:
            for i in range(len(self.free_cells)):
                if self.free_cells[i] is None:
                    self.free_cells[i] = card
                    break

    def move_to_free_column(self, card: Card) -> bool:
        if self.columns.count([]) > 0:
            for i in range(len(self.columns)):
                if not self.columns[i]:
                    self.columns[i].append(card)
                    return True
        return False

    def __move_card_from_free_cell(self, card_to_move: Card, destination_card: Card) -> bool:

        # Check if the move is valid
        if destination_card.is_smaller_and_different_color(card_to_move):
            # Move the card
            self.columns[self.columns.index(destination_card):].append(card_to_move)
            self.free_cells[self.free_cells.index(card_to_move)] = None

            return True

        return False

    def move_to_card(self, card_to_move: Card, destination_card: Card) -> bool:

        if card_to_move.is_smaller_and_different_color(destination_card):

            # Check if card is in free cell
            if card_to_move in self.free_cells:
                return self.__move_card_from_free_cell(card_to_move, destination_card)

            # Check if the move is valid
            # Find the source column and destination column
            source_column = None
            dest_column = None

            # Locate the source column
            for col in self.columns:
                if card_to_move in col:
                    source_column = col
                    break

            # Locate the destination column
            for col in self.columns:
                if destination_card in col:
                    dest_column = col
                    break

            # Check if both source and destination columns are found
            if source_column and dest_column:
                # Determine the cards to move
                cards_to_move = source_column[source_column.index(card_to_move):]

                # Check if there are enough empty cells
                if len(cards_to_move) <= self.empty_cells():
                    # Move the cards
                    dest_column.extend(cards_to_move)
                    source_column = source_column[:source_column.index(card_to_move)]

                    return True  # Move successful
