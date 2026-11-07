from pygame import Rect
import pygame
from constants import *

class Cell(pygame.Rect):
    def __init__(self, size: int, row:int, column:int, color: str):
        super().__init__(row*size, column*size, (row+1)*size, (column+1)*size)
        
        self.cell_size = size
        self.row = row
        self.column = column
        self.color = color
        self.state = "dead"
        self.position = pygame.Vector2(row*size, column*size)
        
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self, LINE_WIDTH)