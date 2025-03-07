from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional
from .character import Character
from .backpack import Backpack
from .point import Point


class Player(Character):

    def __init__(
        self,
        coordinate: Point,
        max_health: int,
        health: int,
        agility: int,
        strength: int,
    ):
        super().__init__(coordinate, health, agility, strength)
        self.max_health: int = max_health
        self.backpack: "Backpack" = Backpack()

    def attack(self) -> int:
        """Calculate and return attack damage"""
        print("Player attacks!")
        return 0
