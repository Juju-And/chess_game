from typing import Optional, List
from abc import ABC

LETTER_FIELDS = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
NUMBER_FIELDS = {
    1: 7,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1,
    8: 0,
}  # "field": array_position


def decode_field(field: str) -> Optional[tuple]:
    if len(field) < 2:  # Ensure the field has at least 2 characters
        return None

    # Extract letter and number
    letter_part = field[0]
    number_part = field[1:]

    try:
        pos_x = LETTER_FIELDS.get(letter_part)
        pos_y = NUMBER_FIELDS.get(int(number_part))
    except ValueError:  # Catch invalid conversion to int
        return None

    # Only return if both positions are valid (not None)
    if pos_x is not None and pos_y is not None:
        return (pos_x, pos_y)

    return None


def code_field(tuple_field: tuple) -> Optional[str]:
    """
    Converts a tuple chessboard position into the corresponding chessboard notation (e.g., (0, 0) -> 'A1').

    Args:
        tuple_field (tuple): Tuple representing the chessboard position, e.g., (0, 1).

    Returns:
        Optional[str]: Chessboard field in string notation, or None if the position is invalid.
    """
    if verify_position_on_chessboard(tuple_field) is not None:
        key_list_letters = list(LETTER_FIELDS.keys())
        val_list_letters = list(LETTER_FIELDS.values())
        key_list_numbers = list(NUMBER_FIELDS.keys())
        val_list_numbers = list(NUMBER_FIELDS.values())

        field_letter = str(key_list_letters[val_list_letters.index(tuple_field[0])])
        field_number = str(key_list_numbers[val_list_numbers.index(tuple_field[1])])

        return field_letter + field_number


def verify_position_on_chessboard(field: tuple) -> Optional[tuple]:
    """
    Validates if the given chessboard field is within the valid range (0 to 7).

    Args:
        field (tuple): Decoded chessboard position, e.g., (0, 1).

    Returns:
        Optional[tuple]: Tuple with field if the position is valid, None otherwise.
    """
    if len(field) != 2:
        return None

    x, y = field
    # Check if both coordinates are within the valid chessboard range (0 to 7)
    if 0 <= x <= 7 and 0 <= y <= 7:
        return field
    return None


class Figure(ABC):
    available_moves = []

    def __init__(self, field):
        self.field = field

    def list_available_moves(self) -> List:
        lst = []
        coded_lst = []
        current_field = decode_field(self.field)

        if current_field is None:
            return []

        for move in self.available_moves:
            if current_field is None:
                return []
            else:
                single_move = tuple(a + b for a, b in zip(move, current_field))
                if verify_position_on_chessboard(single_move) is not None:
                    lst.append(single_move)
        for el in lst:
            coded_lst.append(code_field(el))

        return coded_lst

    def validate_move(self, dest_field: str) -> bool:
        """
        Validate if the destination field is a valid move.

        Args:
            dest_field (str): The target field to validate.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        moves = self.list_available_moves()
        return dest_field in moves


class King(Figure):
    available_moves = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]


class Queen(Figure):
    available_moves = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]


class Rook(Figure):
    available_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up  # down  # left  # right


class Bishop(Figure):
    available_moves = [
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]


class Knight(Figure):
    available_moves = [
        (-2, -1),
        (-2, 1),  # two up, one left/right
        (2, -1),
        (2, 1),  # two down, one left/right
        (-1, -2),
        (-1, 2),  # one up, two left/right
        (1, -2),
        (1, 2),  # one down, two left/right
    ]


class Pawn(Figure):
    available_moves = [(-1, 0), (1, 0)]


CHESS_PIECES = {
    "king": King,
    "queen": Queen,
    "bishop": Bishop,
    "knight": Knight,
    "rook": Rook,
    "pawn": Pawn,
}


def validate_figure(figure: str) -> Optional[str]:
    return CHESS_PIECES.get(figure)
