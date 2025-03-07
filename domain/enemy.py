from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional
from .character import Character
from .point import Point


class Enemy(Character):
    def __init__(
        self,
        coordinate: Point,
        enemy_type: str,
        health: int,
        agility: int,
        strength: int,
        hostility: bool = False,
    ) -> None:
        super().__init__(coordinate, health, agility, strength)
        self.enemy_type: str = enemy_type
        self.hostility: bool = hostility

    def attack(self) -> int:
        """Calculate and return attack damage"""
        print("Enemy attacks!")
        return 0
