from player import Player
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from grid import Grid
import pygame
from constants import *

def main():
    print("Hello from game-of-life!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
    player = Player(grid)
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

                
        screen.fill("black")
        player.update(dt)
        grid.update(dt)
        grid.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
