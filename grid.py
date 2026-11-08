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
    
    # def get_cell(self, row: int, col: int) -> Cell:
    #     index = row * (self.width//self.cell_size) + col
    #     return self.cells[index]

    def get_cell(self, x:int, y:int ) -> Cell:
        index = x//self.cell_size * (self.width//self.cell_size) + y//self.cell_size
        return self.cells[index]
        
    def get_cell(self, coordinates: tuple[int, int]) -> Cell:
        index = coordinates[0]//self.cell_size * (self.height//self.cell_size) + coordinates[1]//self.cell_size
        return self.cells[index]

    