from typing import Tuple, Optional
from .point import Point


class Directions:
    DIRECTIONS = {
        "up": Point(-1, 0),
        "down": Point(1, 0),
        "right": Point(0, 1),
        "left": Point(0, -1),
    }

    OPPOSITE_DIRECTIONS = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left",
    }

    @staticmethod
    def get_direction(direct: str) -> Optional[Point]:
        return Directions.DIRECTIONS.get(direct)

    @staticmethod
    def get_opposite_direction(direct: str) -> Optional[str]:
        return Directions.OPPOSITE_DIRECTIONS.get(direct)

    @staticmethod
    def get_directions() -> Tuple[str, Point]:
        return Directions.DIRECTIONS

    @staticmethod
    def get_opposite_directions() -> Tuple[str, str]:
        return Directions.OPPOSITE_DIRECTIONS
