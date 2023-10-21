import pygame
from typing import Tuple


class Scoreboard:
    scores = [0, 0]

    screen: pygame.Surface
    position: Tuple[int, int]
    rect: pygame.Rect
    text: pygame.Surface

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.Font("pong-font.ttf", 72)

        self.text = self.font.render(
            f"{self.scores[0]} | {self.scores[1]}", False, (200, 200, 200)
        )
        self.rect = self.text.get_rect()
        self.position = (self.screen.get_width() / 2 - self.rect.width / 2, 120)

    def increment(self, player: int):
        if not player:  # No one hit the ball
            return

        if not player in [1, 2]:
            raise ValueError(f"Value outside of number of players: {player=}")

        self.scores[player - 1] += 1
        self.text = self.font.render(
            f"{self.scores[0]} | {self.scores[1]}", False, (200, 200, 200)
        )
        self.rect = self.text.get_rect()
        self.position = (self.screen.get_width() / 2 - self.rect.width / 2, 120)

    def update(self):
        self.screen.blit(self.text, self.position)
