from dataclasses import dataclass
from typing import Optional
import ppb
from ppb import Scene


@dataclass
class InteractRequested:
    position: Optional[ppb.Vector]
    scene: Optional[Scene] = None


@dataclass
class QuitRequested:
    position: Optional[ppb.Vector] = None
    scene: Optional[Scene] = None
