from maze import Maze
from settings import GHOST_SPEED, PACMAN_SPEED, WIDTH, HEIGHT, CELL_SIZE


class Level:
    def __init__(self, level_num):
        self.level_num = level_num
        self.maze = Maze(int(WIDTH / CELL_SIZE), int(HEIGHT / CELL_SIZE), self.level_num) #Maze(WIDTH/CELL_SIZE, HEIGHT/CELL_SIZE, self.level_num)
        self.pacman_speed = PACMAN_SPEED
        self.ghost_speed = GHOST_SPEED
        self.ghosts = self.generate_ghosts()

    def generate_ghosts(self):
        ghosts = [
            {'x': 5, 'y': 5, 'behavior': 'x_first', 'icon': 'assets/ghost1.png'},
            {'x': 10, 'y': 10, 'behavior': 'y_first', 'icon': 'assets/ghost2.png'}
        ]
        return ghosts

    def is_food_collected(self):
        return len(self.maze.food_positions) == 0

    def next_level(self):
        self.level_num += 1
        self.maze = Maze(20, 15, self.level_num)
