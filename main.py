import pygame
from pygame.locals import *
from objects import paddle, ball as b

clock = pygame.time.Clock()

TICK_RATE = 60 # 60fps

def main():
  pygame.init()
  screen = pygame.display.set_mode((720, 500))
  pygame.display.set_caption("Basic pygame")

  bg = pygame.Surface(screen.get_size()).convert()
  bg.fill((30, 30, 30))

  mgr = paddle.PaddleManager(screen)
  ball = b.Ball(24, screen)

  mgr.update()
  ball.update()

  # Draw everything first, text etc
  screen.blit(bg, (0,0))
  pygame.display.flip()

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        return

    # Redraw background
    screen.blit(bg, (0, 0))

    mgr.update()
    ball.update()

    pygame.display.flip()
    clock.tick(TICK_RATE)

if __name__ == '__main__':
  main()
