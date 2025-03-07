from dataclasses import dataclass, field
from typing import List, Tuple, Dict, Optional
from .difficultly import DifficultyLevel
from .level import Level


@dataclass
class GameSession:
    level: "Level" = field(default_factory=lambda: Level())
    difficultly: DifficultyLevel = DifficultyLevel.MEDIUM
