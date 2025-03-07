from dataclasses import dataclass, field
from typing import Set, List, Tuple, Dict, ClassVar
from random import randint
from .enemy import Enemy
from .item import Item
from .door import Door
from .point import Point


@dataclass
class Room:
    ID: Tuple[int, int]

    MIN_HEIGHT: ClassVar[int] = 4
    MAX_HEIGHT: ClassVar[int] = 8
    MIN_WIDTH: ClassVar[int] = 5
    MAX_WIDTH: ClassVar[int] = 25
    HEIGHT: int = field(
        default_factory=lambda: randint(Room.MIN_HEIGHT, Room.MAX_HEIGHT)
    )
    WIDTH: int = field(default_factory=lambda: randint(Room.MIN_WIDTH, Room.MAX_WIDTH))

    doors: list[Door] = field(default_factory=list)
    enemies: list[Enemy] = field(default_factory=list)
    items: list[Item] = field(default_factory=list)
    connected_rooms: Set["Room"] = field(default_factory=set)

    def __post_init__(self) -> None:
        self.local_x: int = randint(0, self.MAX_HEIGHT - self.HEIGHT)
        self.local_y: int = randint(0, self.MAX_WIDTH - self.WIDTH)
        self.l_c: Point = Point(self.local_x, self.local_y)  # local coordinate

    def __hash__(self) -> int:
        return hash(self.ID)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Room):
            return self.ID == other.ID
        return False

    def get_g_c_cell(self, minimal_distance_between_rooms: int) -> Point:
        transform_p1 = Point(Room.MAX_HEIGHT, Room.MAX_WIDTH)
        transform_p2 = Point(
            minimal_distance_between_rooms, minimal_distance_between_rooms
        )
        transform_p = transform_p1 + transform_p2
        return Point(self.ID) * transform_p + transform_p2
