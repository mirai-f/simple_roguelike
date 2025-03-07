from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional
from random import randint
from .direction import Directions
from .point import Point

from icecream import ic  # type: ignore


@dataclass
class Corridor:
    id: Tuple[Tuple[int, int], Tuple[int, int]]
    path: List[Point] = field(default_factory=list)

    def generate_path(self, direct: str, p_out: Point, p_in: Point) -> List[Point]:
        path: List[Point] = []

        start = p_out + Directions.get_direction(direct)
        end = p_in + Directions.get_direction(Directions.get_opposite_direction(direct))

        if direct in {"up", "down"}:
            turn_x = randint(min(start[0], end[0]), max(start[0], end[0]))

            step_x = 1 if start[0] < turn_x else -1
            path.extend(Point(i, start[1]) for i in range(start[0], turn_x, step_x))

            step_y = 1 if start[1] < end[1] else -1
            path.extend(Point(turn_x, j) for j in range(start[1], end[1], step_y))

            step_x = 1 if turn_x < end[0] else -1
            path.extend(
                Point(i, end[1]) for i in range(turn_x, end[0] + step_x, step_x)
            )
        else:
            turn_y = randint(min(start[1], end[1]), max(start[1], end[1]))

            step_y = 1 if start[1] < turn_y else -1
            path.extend(Point(start[0], j) for j in range(start[1], turn_y, step_y))

            step_x = 1 if start[0] < end[0] else -1
            path.extend(Point(i, turn_y) for i in range(start[0], end[0], step_x))

            step_y = 1 if turn_y < end[1] else -1
            path.extend(
                Point(end[0], j) for j in range(turn_y, end[1] + step_y, step_y)
            )

        self.path = path
