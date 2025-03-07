from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional
from .item import Item


@dataclass
class Backpack:
    items: List["Item"] = field(default_factory=list)
