from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from grid import Grid
import pygame
from constants import *

def main():
    print("Hello from game-of-life!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")

    grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
    grid.draw(screen)
    while True:
        pygame.display.flip()  


if __name__ == "__main__":
    main()
