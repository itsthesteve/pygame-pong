import pygame
from pygame.locals import *
import objects.paddle as p
# YAH: import objects.ball

clock = pygame.time.Clock()

TICK_RATE = 60 # 60fps

def main():
  pygame.init()
  screen = pygame.display.set_mode((720, 500))
  pygame.display.set_caption("Basic pygame")

  bg = pygame.Surface(screen.get_size()).convert()
  bg.fill((30, 30, 30))

  mgr = p.PaddleManager(screen)
  mgr.draw()

  screen.blit(bg, (0,0))
  pygame.display.flip()

  while True:
    clock.tick(TICK_RATE)

    for event in pygame.event.get():
      if event.type == QUIT:
        return

    screen.blit(bg, (0, 0))

    mgr.listen_for_keys()
    mgr.draw()

    pygame.display.flip()

if __name__ == '__main__':
  main()
