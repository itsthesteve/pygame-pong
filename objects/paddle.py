import pygame
from typing import List, Tuple
from pygame.locals import K_DOWN, K_UP

# Increase this to make the paddle smaller
PADDLE_SIZE_DIVISOR = 4
PADDLE_WIDTH = 20

class Paddle():
  srf: pygame.Surface
  x: int
  y: int

  def __init__(self, size: Tuple[int, int], x: int):
    self.srf = pygame.Surface(size)
    self.srf.fill((255, 255, 255))
    self.srf.convert()

    self.x = x
    self.y = 0

  @property
  def position(self) -> Tuple[int, int]:
    return (self.x, self.y)

class PaddleManager():
  paddles: List[Paddle]
  screen: pygame.Surface
  max_y: int

  def __init__(self, screen: pygame.Surface):
    PADDLE_HEIGHT = screen.get_height() / PADDLE_SIZE_DIVISOR

    self.screen = screen
    self.max_y = self.screen.get_height() - PADDLE_HEIGHT

    p1 = Paddle((PADDLE_WIDTH, PADDLE_HEIGHT), 0)
    p2 = Paddle((PADDLE_WIDTH, PADDLE_HEIGHT), self.screen.get_width() - PADDLE_WIDTH)

    self.paddles = [p1, p2]

  def draw(self):
    for p in self.paddles:
      self.screen.blit(p.srf, p.position)

  def listen_for_keys(self) -> None:
    keys = pygame.key.get_pressed()
    p1, _ = self.paddles

    if keys[K_DOWN]:
      if p1.y <= self.max_y:
        p1.y += 10
    if keys[K_UP]:
      if p1.y >= 0:
        p1.y -= 10
