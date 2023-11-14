from game.Card import Card


class Board:
    """
    Represents a FreeCell game board.

    The board consists of columns, free cells, and suit stacks where cards are placed. The goal of the game
    is to move all cards to the suit stacks while following the rules of the game.

    Args:
        cards (list): A list of card objects to initialize the game board.

    Attributes:
        columns (list of list): The columns on the board, represented as lists of cards.
        free_cells (list of Card or None): The free cells, each holding a card or None.
        suit_stack (dict): A dictionary representing the suit stacks for hearts (h), diamonds (d), clubs (c), and spades (s).

    Methods:
        - empty_cells(): Returns the number of empty cells in the columns and free cells.
        - move_to_stack(card): Attempts to move a card to a suit stack.
        - move_to_free_cell(card): Attempts to move a card to a free cell.
        - move_to_free_column(card): Attempts to move a card to an empty column.
        - move_to_card(card_to_move, destination_card): Attempts to move a card to another card.
    """

    def __init__(self, cards: list) -> None:
        self.columns = []
        self.free_cells = [None for _ in range(4)]
        self.suit_stack = {"h": None, "d": None, "c": None, "s": None}
        self.__make_deck(cards)

    def __is_on_top(self, card: Card) -> list:
        """
        Finds the column containing the given card if it is on top.

        Args:
            card (Card): The card to search for.

        Returns:
            list: The column that contains the card if it's on top, otherwise an empty list.
        """
        col = next((col for col in self.columns if col and card == col[-1]), [])

        return col

    def __move_card_from_free_cell_to_card(
        self, card_to_move: Card, destination_card: Card
    ) -> bool:
        """
        Moves a card from a free cell to another card.

        Args:
            card_to_move (Card): The card to be moved.
            destination_card (Card): The card where the move is attempted.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        self.columns[
            next(i for i, col in enumerate(self.columns) if destination_card in col)
        ].append(card_to_move)
        self.free_cells[self.free_cells.index(card_to_move)] = None
        return True

    def __move_card_from_free_cell_to_empty_column(self, card_to_move: Card) -> bool:
        """
        Moves a card from a free cell to an empty column.

        Args:
            card_to_move (Card): The card to be moved.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        self.columns[next(i for i, col in enumerate(self.columns) if not col)].append(
            card_to_move
        )
        self.free_cells[self.free_cells.index(card_to_move)] = None
        return True

    def __make_deck(self, cards: list) -> None:
        """
        Initializes the columns with cards from a provided list.

        Args:
            cards (list): A list of card objects to distribute across the columns.
        """
        start = 0
        cards_per_column = [6] * 4 + [7] * 4

        for num_cards in cards_per_column:
            column = cards[start : start + num_cards]
            self.columns.append(column)
            start += num_cards

    def empty_cells(self) -> int:
        """
        Returns the number of empty cells in the columns and free cells.

        Returns:
            int: The number of empty cells.
        """
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

    def find_card_from_string(self, card_string: str) -> Card:
        """Find a card from a string.

        :param card_string: A string representing a card.
        :return: A Card object if it is at the top of any column
        or free cells, else None.
        """
        for column in self.columns:
            if column and str(column[-1]) == card_string:
                return column[-1]
        for card in self.free_cells:
            if card and str(card) == card_string:
                return card
        return None

    def move_to_stack(self, card: Card) -> bool:
        """
        Attempts to move a card to a suit stack.

        Args:
            card (Card): The card to be moved.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if card in self.free_cells:
            if card.is_larger_and_same_suit(self.suit_stack[card.suit]):
                self.suit_stack[card.suit] = card
                self.free_cells[self.free_cells.index(card)] = None
                return True
            return False

        col = self.__is_on_top(card)

        if not col:
            return False

        if card.is_larger_and_same_suit(self.suit_stack[card.suit]):
            self.suit_stack[card.suit] = card
            col.pop()
            return True

        return False

    def move_to_free_cell(self, card: Card) -> bool:
        """
        Attempts to move a card to a free cell.

        Args:
            card (Card): The card to be moved.

        Returns:
            bool: True if the move was successful, False otherwise.
        """

        col = self.__is_on_top(card)

        if not col:
            return False

        if self.free_cells.count(None) > 0:
            for i in range(len(self.free_cells)):
                if self.free_cells[i] is None:
                    self.free_cells[i] = card
                    col.pop()
                    return True

    def move_to_free_column(self, card: Card) -> bool:
        """
        Attempts to move a card to an empty column.

        Args:
            card (Card): The card to be moved.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        # check if there is any free column
        if self.columns.count([]) < 1:
            return False

        if card in self.free_cells:
            return self.__move_card_from_free_cell_to_empty_column(card)

        source_col = self.__is_on_top(card)
        dest_col = next(col for col in self.columns if not col)

        dest_col.append(source_col.pop())
        return True
        

        # source_column = next((col for col in self.columns if card in col), None)
        # if source_column:
        #     cards_to_move = source_column[source_column.index(card) :]

        #     valid_sequence = all(
        #         card.is_smaller_and_different_color(prev_card)
        #         for card, prev_card in zip(cards_to_move[1:], cards_to_move)
        #     )

        #     if len(cards_to_move) <= self.empty_cells() and valid_sequence:
        #         self.columns[
        #             next(i for i, col in enumerate(self.columns) if not col)
        #         ].extend(cards_to_move)

        #         index_of_card_to_move = source_column.index(card)
        #         source_column[index_of_card_to_move:] = source_column[
        #             :index_of_card_to_move
        #         ]

        #         return True  # Move successful

        # return False  # Move unsuccessful

    def __move_card_from_free_cell_to_card(
        self, card_to_move: Card, destination_card: Card
    ) -> bool:
        self.columns[
            next(i for i, col in enumerate(self.columns) if destination_card in col)
        ].append(card_to_move)

        self.free_cells[self.free_cells.index(card_to_move)] = None
        return True

    def __move_card_from_free_cell_to_empty_column(self, card_to_move: Card) -> bool:
        self.columns[next(i for i, col in enumerate(self.columns) if not col)].append(
            card_to_move
        )
        self.free_cells[self.free_cells.index(card_to_move)] = None
        return True

    def move_to_card(self, card_to_move: Card, destination_card: Card) -> bool:
        """
        Attempts to move a card to another card.

        Args:
            card_to_move (Card): The card to be moved.
            destination_card (Card): The card where the move is attempted.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if card_to_move.is_smaller_and_different_color(destination_card):
            # Check if card is in free cell
            if card_to_move in self.free_cells:
                return self.__move_card_from_free_cell_to_card(
                    card_to_move, destination_card
                )

            dest_column = self.__is_on_top(destination_card)
            source_column = self.__is_on_top(card_to_move)

            if dest_column and source_column:
                dest_column.append(source_column.pop())
                return True  # Move successful

        return False
