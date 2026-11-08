import random
from constants import COLOR
import pygame
from cell import Cell

class Grid:
    def __init__(self, width: int, height: int, cell_size: int):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells: list[Cell] = []

        for x in range(width//cell_size):
            for y in range(height//cell_size):
                self.cells.append(Cell(self.cell_size, x, y, COLOR))

    def draw(self, screen: pygame.Surface) -> None:
        for cell in self.cells:
            cell.draw(screen)
    
    def born_random(self):
        index = random.randint(0, len(self.cells)-1)
        cell = self.cells[index]
        print(cell)
        cell.state = "alive"


    