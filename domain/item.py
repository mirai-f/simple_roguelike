from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional
from abc import ABC, abstractmethod


@dataclass
class Item:
    type: str
    subtype: Optional[str] = None
    health_increase: Optional[int] = None
    max_health_increase: Optional[int] = None
    agility_increase: Optional[int] = None
    strength_increase: Optional[int] = None
    value: Optional[int] = None
