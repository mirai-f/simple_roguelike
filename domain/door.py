from typing import NamedTuple
from .point import Point


class Door(NamedTuple):
    direction: str
    l_c: Point
