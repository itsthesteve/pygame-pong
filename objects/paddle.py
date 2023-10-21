import pygame
from typing import List, Tuple
from pygame.locals import K_DOWN, K_UP

# Increase this to make the paddle smaller
PADDLE_SIZE_DIVISOR = 4
PADDLE_WIDTH = 20

class Paddle():
  srf: pygame.Surface
  rect: pygame.Rect
  _x: int
  _y: int

  def __init__(self, size: Tuple[int, int], x: int):
    self.rect = pygame.Rect(0, 0, size[0], size[1])
    # self.srf = pygame.Surface(size)
    # self.srf.fill((255, 255, 255))
    # self.srf.convert()

    self.rect.x = x
    self.rect.y = 0

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

  def update(self, ball) -> None:
    """
    Update the Y coordinate for the player 1 paddle, keeping it within
    the top and bottom constraints.
    TODO: Maybe a built-in exists for this
    """
    keys = pygame.key.get_pressed()
    p1, p2 = self.paddles

    if keys[K_DOWN]:
      if p1.rect.y <= self.max_y:
        p1.rect.y += 10
    if keys[K_UP]:
      if p1.rect.y >= 0:
        p1.rect.y -= 10

    # Detect collision with right edge of paddle 1
    if p1.rect.colliderect(ball.rect):
      if abs(ball.rect.left <= p1.rect.right):
        ball.bounce()

    # Detect collision with left edge of paddle 2
    if p2.rect.colliderect(ball.rect):
      if abs(ball.rect.right >= p1.rect.left):
        ball.bounce()

    for p in self.paddles:
      # self.screen.blit(p.srf, p.position)
      pygame.draw.rect(self.screen, (255, 255, 255), p.rect)
