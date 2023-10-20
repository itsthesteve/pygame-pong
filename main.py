import pygame
from pygame.locals import *
import objects.paddle as p

clock = pygame.time.Clock()

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
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        return

    screen.blit(bg, (0, 0))

    mgr.listen_for_keys()
    mgr.draw()

    pygame.display.flip()

if __name__ == '__main__':
  main()
