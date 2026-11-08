import random
from constants import COLOR, SIMULATION_SPEED
import pygame
from cell import Cell

class Grid:
    def __init__(self, width: int, height: int, cell_size: int):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.columns = width//cell_size
        self.rows = height//cell_size
        self.cells: list[Cell] = []
        self.update_timer = 0.0

        for x in range(self.columns):
            for y in range(self.rows):
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

    # def get_cell(self, row:int, col:int ) -> Cell:
    #     index = x//self.cell_size * (self.columns) + y//self.cell_size
    #     return self.cells[index]
        
    def get_cell_at(self, coordinates_pixels: tuple[int, int]) -> Cell:
        index = coordinates_pixels[0]//self.cell_size * (self.rows) + coordinates_pixels[1]//self.cell_size
        # print(f"clicked cell on column:{coordinates_pixels[0]//self.cell_size} and row:{coordinates_pixels[1]//self.cell_size}")
        # print(f"index: {index}")
        return self.cells[index]
    
    def get_cell_index_at(self, coordinates_pixels: tuple[int, int]) -> int:
        return coordinates_pixels[0]//self.cell_size * (self.rows) + coordinates_pixels[1]//self.cell_size


    def get_neighbours(self, cell_index: int) -> list[Cell]:
        neighbours = []
        index_diffs = [
            cell_index - self.rows - 1, 
            cell_index - self.rows, 
            cell_index - self.rows + 1, 
            cell_index - 1,
            cell_index + 1,
            cell_index + self.rows - 1,
            cell_index + self.rows,
            cell_index + self.rows + 1]
        for i in range(len(index_diffs)):
            this_row = cell_index%self.rows
            that_row = index_diffs[i]%self.rows 
            if abs(that_row - this_row) > 1:
                index_diffs[i] = -1
        for i in index_diffs:
            if i >=0 and i <= len(self.cells) - 1:
                neighbours.append(self.cells[i])
        return neighbours

    def count_alive(self, cells: list[Cell]) -> int:
        counter = 0
        for cell in cells:
            if cell.state == "alive":
                counter += 1
        return counter

    def apply_state_mask(self, mask: bool):
        for i in range(len(self.cells)):
            if mask[i]:
                self.cells[i].state = "alive"
            else:
                self.cells[i].state = "dead"
            

    def update(self, dt: float):
        self.update_timer += dt
        print(f"timer: {self.update_timer}, dt: {dt}")
        if (self.update_timer >= SIMULATION_SPEED):
            self.update_timer = 0.0
            state_mask = []
            for i in range(len(self.cells)):
                alive_count = self.count_alive(self.get_neighbours(i))
                print(f"i: {i}, alive: {alive_count}")
                if (alive_count == 2 and self.cells[i].state == "alive") or alive_count == 3:
                    state_mask.append(True)
                else:
                    state_mask.append(False)
            print(f"{state_mask}")
            self.apply_state_mask(state_mask)
                
            
        
    