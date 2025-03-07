from math import sqrt
from typing import Tuple, Union, Optional


class Point:
    def __init__(
        self, x_or_coordinates: Union[Tuple[int, int], int], y: Optional[int] = None
    ):
        if isinstance(x_or_coordinates, tuple):  # Если передан кортеж
            self.x, self.y = x_or_coordinates
        elif y is not None:  # Если переданы два значения
            self.x = x_or_coordinates
            self.y = y
        else:
            raise ValueError(
                "Invalid arguments: either provide a tuple or two integer values."
            )

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, "Point"]) -> "Point":
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        elif isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        else:
            raise TypeError(
                "Multiplication is supported only with an integer, float, or another Point."
            )

    def __rmul__(self, other: int) -> "Point":
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError(
                "Multiplication is supported only with an integer or float."
            )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return not self.__eq__(other)

    def __gt__(self, other: "Point") -> bool:
        if not isinstance(other, Point):
            raise TypeError(
                "Comparison not supported between instances of 'Point' and other types"
            )
        return (self.x, self.y) > (other.x, other.y)

    def __ge__(self, other: "Point") -> bool:
        if not isinstance(other, Point):
            raise TypeError(
                "Comparison not supported between instances of 'Point' and other types"
            )
        return (self.x, self.y) >= (other.x, other.y)

    def __lt__(self, other: "Point") -> bool:
        if not isinstance(other, Point):
            raise TypeError(
                "Comparison not supported between instances of 'Point' and other types"
            )
        return (self.x, self.y) < (other.x, other.y)

    def __le__(self, other: "Point") -> bool:
        if not isinstance(other, Point):
            raise TypeError(
                "Comparison not supported between instances of 'Point' and other types"
            )
        return (self.x, self.y) <= (other.x, other.y)

    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, index: int) -> int:
        try:
            return (self.x, self.y)[index]
        except IndexError:
            raise IndexError("Point index out of range. Valid indices: 0 (x), 1 (y).")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other: "Point") -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
