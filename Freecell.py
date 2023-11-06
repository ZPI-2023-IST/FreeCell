from Game import Game, State
from Board import Board
from Deck import Deck
from Move import Move


class FreeCell(Game):
    def __init__(self):
        self._move_count = 0
        self.deck = Deck()
        self.board = Board(self.deck.cards_shuffled())

    def increment_move_count(self):
        self._move_count += 1

    # Overridden functions from Game class

    def get_all_moves(self) -> list:
        """Get all possible moves from the current board state.

        :return: A list of all possible moves from the current board state.

        :notation: A move is a tuple of the form (card, destination), where:
            * card is the card to be moved
            * destination is either:
                - 'F'
                for freecell
                - 'S'
                for suit stack
                - '{rank}{color}'
                card for any other destination card.
                - '0'
                for empty columns
            * examples:
                - ('TH', 'F')
                means moving the Ten of Hearts to a freecell
                - ('JS', 'S')
                means moving the Jack of Spades to a suit stack
                - ('AD', '2C')
                means moving the Ace of Diamonds to the 2 of Clubs
                - ('AD', '0')
                means moving the Ace of Diamonds to an empty column
        """
        moves = list()

        # Moves onto empty columns
        if [] in self.board.columns:
            for card in self.board.free_cells + self.board.get_movable_cards():
                if card:
                    moves.append((str(card), '0'))

        # Get cards from the top of columns
        suspected_moves = self.board.get_movable_cards()

        # Check if at least one of freecells is empty
        if None in self.board.free_cells:
            # Append moving every from the top of column to a freecell
            for card in suspected_moves:
                moves.append((str(card), 'F'))

        for card in self.board.free_cells:
            if card:
                # Check for suit stack moves
                if card.is_larger_and_same_suit(
                        self.board.suit_stack[card.suit]):
                    moves.append((str(card), 'S'))

                # Check if any card from freecells can be moved onto a column
                for card_destination in suspected_moves:
                    if card.is_smaller_and_different_color(card_destination):
                        moves.append((str(card), str(card_destination)))

        for card in suspected_moves:
            # Check if any card from columns can be moved onto a suit stack
            if card.is_larger_and_same_suit(self.board.suit_stack[card.suit]):
                moves.append((str(card), 'S'))

            # Check if any card from columns can be moved onto another column
            for card_destination in suspected_moves:
                if card != card_destination and (
                        card.is_smaller_and_different_color(card_destination)):
                    moves.append((str(card), str(card_destination)))

        return moves

    def make_move(self, move: tuple) -> bool:
        if move not in self.get_all_moves():
            return False

        card = self.board.find_card_from_string(move[0])
        match move[1]:
            case Move.FREECELL.value:
                self.board.move_to_free_cell(card)
            case Move.SUIT_STACK.value:
                self.board.move_to_stack(card)
            case Move.EMPTY_COLUMN.value:
                self.board.move_to_free_column(card)
            case _:
                self.board.move_to_card(
                    card, self.board.find_card_from_string(move[1]))
        self.increment_move_count()
        return True

    def get_state(self) -> State:
        """Get the current state of the game.

        :return: The current state of the game as State enum.
        """
        suit_stack = list(self.board.suit_stack.values())
        for card in suit_stack:
            if card is None or card.rank != 13:
                return State.ONGOING if bool(
                    self.get_all_moves()) else State.LOST
        return State.WON

    def get_board(self) -> list:
        """Get the current board state.

        :return: The current board state as a list of 10 lists:
            * The first 8 lists are the columns.
            * The next 4 element long list is the list of free cells.
            * The last 4 element long list is
              the list of the top cards on each suit stack.
        """
        return self.board.columns + [self.board.free_cells] + [list(
            self.board.suit_stack.values())]
