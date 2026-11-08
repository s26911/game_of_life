import sys
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
        self.timer = 0.0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.grid.born_random()
            self.timer = 0.0
        if keys[pygame.K_q]:
            sys.exit()
        if keys[pygame.K_c]:
            self.grid.clear()
        if keys[pygame.K_SPACE]:
            self.grid.paused = True
        else:
            self.grid.paused = False


        left, middle, right = pygame.mouse.get_pressed()
        if left:
            cell = self.grid.get_cell_at(pygame.mouse.get_pos())
            cell.state = "alive"
        if right:
            cell = self.grid.get_cell_at(pygame.mouse.get_pos())
            cell.state = "dead"
        if middle:
            pass
        
        coordinates = pygame.mouse.get_pos()
        self.grid.hovered = self.grid.get_cell_at(coordinates)
