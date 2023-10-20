from pygame import Surface
from typing import Tuple

class Ball():
  x: int
  y: int
  bounds: Tuple[int, int]
  srf: Surface

  def __init__(self, size: int, bounds: Tuple[int, int]) -> Surface:
    self.x = 0
    self.y = 0
    self.bounds = bounds

    self.srf = Surface((size, size))
    self.srf.fill((255, 255, 255))
    self.srf.convert()

    return self.srf

  def draw(self, coords: Tuple[int, int]) -> None:
    ...

  def update(self):
    ...
