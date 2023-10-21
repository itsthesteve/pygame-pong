import pygame
from typing import Tuple


class Ball():
  x: int
  y: int
  rect: pygame.Rect
  screen: pygame.Surface
  _bounds: Tuple[int, int]
  _center: Tuple[int, int]
  _vel_x: int = 3
  _vel_y: int = 3

  def __init__(self, size: int, screen: pygame.Surface):
    self._bounds = screen.get_size()

    self.screen = screen
    self.size = size

    w, h = self._bounds

    # default to draw in the center of the screen
    self.x = w / 2 - (self.size / 2)
    self.y = h / 2 - (self.size / 2)
    self.rect = pygame.Rect(self.x, self.y, size, size)

  def update(self):
    self.rect.x += self._vel_x
    self.rect.y += self._vel_y

    if self.rect.right >= self._bounds[0] or self.rect.left <= 0:
      self._vel_x = -self._vel_x

    if self.rect.bottom >= self._bounds[1] or self.rect.top <= 0:
      self._vel_y = -self._vel_y

    pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
