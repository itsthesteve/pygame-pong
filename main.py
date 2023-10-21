import pygame
from pygame.locals import *
from objects import paddle, ball as b, events as ev

clock = pygame.time.Clock()

TICK_RATE = 60 # 60fps

def main():
  pygame.init()
  screen = pygame.display.set_mode((720, 500))
  score = 0

  title_font = pygame.font.Font("pong-font.ttf", 32)
  score_font = pygame.font.Font("pong-font.ttf", 144)

  title_text = title_font.render("Pong", True, (100, 100, 100))
  score_text = score_font.render(str(score), True, (200, 200, 200))

  title_text_rect = title_text.get_rect()
  title_text_pos = (screen.get_width() / 2 - title_text_rect.width / 2, 32)

  score_text_rect = score_text.get_rect()
  score_text_pos = (screen.get_width() / 2 - score_text_rect.width / 2, 72)

  pygame.display.set_caption("Pong")

  bg = pygame.Surface(screen.get_size()).convert()
  bg.fill((30, 30, 30))

  mgr = paddle.PaddleManager(screen)
  ball = b.Ball(24, screen)

  mgr.update(ball)
  ball.update()

  # Draw everything first, text etc
  screen.blit(bg, (0,0))
  pygame.display.flip()

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      if event.type == ev.OUT_OF_BOUNDS:
        if mgr.last_touch and mgr.last_touch.player_num == 1:
          score += 1
          score_text = score_font.render(str(score), True, (200, 200, 200))
          mgr.last_touch = None

    # Redraw background
    screen.blit(bg, (0, 0))
    screen.blit(title_text, title_text_pos)
    screen.blit(score_text, score_text_pos)

    mgr.update(ball)
    ball.update()

    pygame.display.flip()
    clock.tick(TICK_RATE)

if __name__ == '__main__':
  main()
