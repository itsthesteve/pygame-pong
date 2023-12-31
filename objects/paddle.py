from typing import List, Tuple

import pygame
from pygame.locals import K_DOWN, K_UP, K_s, K_w

from .events import PADDLE_HIT

# Increase this to make the paddle smaller
PADDLE_SIZE_DIVISOR = 4
PADDLE_WIDTH = 20
EDGE_MARGIN = 10


class Paddle:
    srf: pygame.Surface
    rect: pygame.Rect
    player_num: int

    def __init__(self, size: Tuple[int, int], coords: Tuple[int, int], player_num: int):
        x, y = coords

        self.rect = pygame.Rect(x, y, size[0], size[1])
        self.rect.x = x
        self.rect.y = y
        self.player_num = player_num

    def __repr__(self):
        return f"<Paddle: {self.player_num=} @ ({self.rect=})>"


class PaddleManager:
    paddles: List[Paddle]
    _screen: pygame.Surface
    _max_y: int

    def __init__(self, screen: pygame.Surface):
        PADDLE_HEIGHT = screen.get_height() / PADDLE_SIZE_DIVISOR

        self._screen = screen
        self._max_y = self._screen.get_height() - PADDLE_HEIGHT

        center_y = self._screen.get_height() / 2 - PADDLE_HEIGHT / 2

        p1 = Paddle(
            (PADDLE_WIDTH, PADDLE_HEIGHT), (EDGE_MARGIN, center_y), player_num=1
        )
        p2 = Paddle(
            (PADDLE_WIDTH, PADDLE_HEIGHT),
            (self._screen.get_width() - PADDLE_WIDTH - EDGE_MARGIN, center_y),
            player_num=2,
        )

        self.paddles = [p1, p2]

    def update(self, ball) -> None:
        """
        Update the Y coordinate for the player 1 paddle, keeping it within
        the top and bottom constraints.
        TODO: Maybe a built-in exists for this
        """
        keys = pygame.key.get_pressed()
        p1, p2 = self.paddles

        # player 1
        if keys[K_DOWN]:
            if p1.rect.y <= self._max_y:
                p1.rect.y += 10
        if keys[K_UP]:
            if p1.rect.y >= 0:
                p1.rect.y -= 10

        # player 2
        if keys[K_s]:
            if p2.rect.y <= self._max_y:
                p2.rect.y += 10
        if keys[K_w]:
            if p2.rect.y >= 0:
                p2.rect.y -= 10

        # Detect collision with right edge of paddle 1
        if p1.rect.colliderect(ball.rect):
            if abs(ball.rect.left <= p1.rect.right):
                ball.bounce()
                pygame.event.post(pygame.event.Event(PADDLE_HIT, {"player": 1}))

        # Detect collision with left edge of paddle 2
        if p2.rect.colliderect(ball.rect):
            if abs(ball.rect.right >= p1.rect.left):
                ball.bounce()
                pygame.event.post(pygame.event.Event(PADDLE_HIT, {"player": 2}))

        for p in self.paddles:
            pygame.draw.rect(self._screen, (255, 255, 255), p.rect)
