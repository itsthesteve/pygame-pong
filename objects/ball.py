from pygame import Surface
from typing import Tuple

SPEED = 5

class Ball():
  x: int
  y: int
  srf: Surface
  screen: Surface
  _bounds: Tuple[int, int]
  _center: Tuple[int, int]
  _vel_x: int = SPEED
  _vel_y: int = SPEED

  def __init__(self, size: int, screen: Surface):
    self.screen = screen
    self.size = size
    self._bounds = screen.get_size()
    w, h = self._bounds

    # default to center of the screen
    self.x = w / 2 - (self.size / 2)
    self.y = h / 2 - (self.size / 2)

    self.srf = Surface((size, size))
    self.srf.fill((255, 255, 255))
    self.srf.convert()

  def update(self):
    # YAH: Do collision stuff
    self.x = self.x + self._vel_x
    self.y = self.y + self._vel_y
    if (self.x >= self._bounds[0] - self.size):
      self._vel_x = -SPEED

    if (self.x <= 0):
      self._vel_x = SPEED

    if (self.y >= self._bounds[1] - self.size):
      self._vel_y = -SPEED

    if (self.y <= 0):
      self._vel_y = SPEED

    self.screen.blit(self.srf, (self.x, self.y))
