import pygame
from pygame.locals import *
from objects import paddle, ball as b, events as ev, scoreboard

clock = pygame.time.Clock()

TICK_RATE = 60 # 60fps

def main():
  pygame.init()
  screen = pygame.display.set_mode((720, 512))

  title_font = pygame.font.Font("pong-font.ttf", 32)
  title_text = title_font.render("Pong", True, (100, 100, 100))

  title_text_rect = title_text.get_rect()
  title_text_pos = (screen.get_width() / 2 - title_text_rect.width / 2, 32)

  pygame.display.set_caption("Pong")

  bg = pygame.Surface(screen.get_size()).convert()
  bg.fill((30, 30, 30))

  mgr = paddle.PaddleManager(screen)
  ball = b.Ball(24, screen)
  score = scoreboard.Scoreboard(screen)

  mgr.update(ball)
  ball.update()
  score.update()

  screen.blit(bg, (0,0))
  screen.blit(title_text, title_text_pos)
  pygame.display.flip()

  # Last player that hit the ball
  paddle_hit_player: int = None

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        return

      if event.type == ev.PADDLE_HIT:
        paddle_hit_player = event.player

      if event.type == ev.OUT_OF_BOUNDS:
        score.increment(paddle_hit_player)
        paddle_hit_player = None

    # Redraw background
    screen.blit(bg, (0, 0))
    screen.blit(title_text, title_text_pos)

    mgr.update(ball)
    ball.update()
    score.update()

    pygame.display.flip()
    clock.tick(TICK_RATE)

if __name__ == '__main__':
  main()
