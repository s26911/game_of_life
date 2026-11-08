from constants import KEY_PRESS_COOLDOWN
from grid import Grid
import grid
import pygame

class Player:
    def __init__(self, grid: Grid):
        self.grid = grid
        self.timer = 0.0

    def update(self, dt) -> None:
        if self.timer < KEY_PRESS_COOLDOWN:
            self.timer += dt
            return
        keys = pygame.key.get_pressed()

        if keys[pygame.K_r]:
            self.grid.born_random()
            self.timer = 0.0

