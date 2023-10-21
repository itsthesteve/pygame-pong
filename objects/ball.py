import pygame
from typing import Tuple
from .events import OUT_OF_BOUNDS
from random import randrange


class Ball:
    x: int
    y: int
    rect: pygame.Rect
    screen: pygame.Surface
    _bounds: Tuple[int, int]
    _center: Tuple[int, int]
    _vel_x: int
    _vel_y: int

    def __init__(self, size: int, screen: pygame.Surface):
        self._set_velocities()
        self.screen = screen
        self.size = size

        self._bounds = screen.get_size()
        self._center = (
            self._bounds[0] / 2 - (self.size / 2),
            self._bounds[1] / 2 - (self.size / 2),
        )

        self.rect = pygame.Rect(self._center[0], self._center[1], size, size)

    def _set_velocities(self):
        """
        Randomize the values of the start x and y velocity
        Probably a better way to do this
        """
        rand_seed = randrange(0, 10)
        self._vel_x = -4 if rand_seed < 5 else 4
        self._vel_y = self._vel_x

    def bounce(self) -> None:
        self._vel_x = -self._vel_x

    def reset(self) -> None:
        """
        Draw at the center of the screen
        """
        self._set_velocities()
        x, y = self._center
        self.rect.x = x
        self.rect.y = y
        self._vel_x = -4
        self._vel_y = -4

    def update(self) -> None:
        """
        TODO: Lose when it hits the edge as opposed to bouncing
        """
        self.rect.x += self._vel_x
        self.rect.y += self._vel_y

        if self.rect.left <= 0 or self.rect.right >= self._bounds[0]:
            pygame.event.post(pygame.event.Event(OUT_OF_BOUNDS))
            self.reset()

        if self.rect.bottom >= self._bounds[1] or self.rect.top <= 0:
            self._vel_y = -self._vel_y

        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
