import pygame
from typing import Tuple
from pygame.locals import *

clock = pygame.time.Clock()

def render_paddle(height: int) -> None:
  paddle = pygame.Surface((20, height))
  paddle.fill((255, 255, 255))

  return paddle

def main():
  pygame.init()
  screen = pygame.display.set_mode((720, 500))
  pygame.display.set_caption("Basic pygame")

  screen_height = screen.get_height()
  paddle_height = screen.get_height() / 4

  bg = pygame.Surface(screen.get_size()).convert()
  bg.fill((30, 30, 30))

  p2 = render_paddle(paddle_height)
  p1 = render_paddle(paddle_height)

  screen.blit(p1, (0, 0))
  screen.blit(p2, (screen.get_width() - 25, 0))
  screen.blit(bg, (0,0))

  pygame.display.flip()

  cur_y = 0

  run = True
  while run:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        return

    keys = pygame.key.get_pressed()
    if keys[K_DOWN]:
      cur_y += 10
    if keys[K_UP]:
      cur_y -= 10

    if cur_y <= 0:
      cur_y = 0

    if cur_y >= screen_height - paddle_height:
      cur_y = screen_height - paddle_height

    screen.blit(bg, (0, 0))
    screen.blit(p1, (0, cur_y))
    screen.blit(p2, (screen.get_width() - 25, 0))
    pygame.display.flip()

if __name__ == '__main__':
  main()
