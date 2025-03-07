from typing import Tuple
from abc import ABC, abstractmethod
from .point import Point


class Character(ABC):
    def __init__(self, l_c: Point, health: int, agility: int, strength: int) -> None:
        self.l_c: Point = l_c
        self.health: int = health
        self.agility: int = agility
        self.strength: int = strength

    def is_alive(self) -> bool:
        return self.health > 0

    def get_position(self) -> Point:
        return self.l_c

    def move(self, dp: Point) -> None:
        self.l_c += dp

    @abstractmethod
    def attack(self) -> int:  # Добавляем self как первый аргумент
        """Calculate and return attack damage"""
