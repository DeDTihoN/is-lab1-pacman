import random
import pygame
from settings import CELL_SIZE, FOOD_ICON

class Maze:
    def __init__(self, width, height, level):
        self.width = width
        self.height = height
        self.level = level
        self.maze = self.generate_maze()

        # Завантаження іконки їжі
        self.food_icon = pygame.image.load(FOOD_ICON).convert_alpha()
        self.food_positions = self.generate_food()

    def generate_maze(self):
        maze = [['#'] * self.width for _ in range(self.height)]
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                if random.random() > 0.0:
                    maze[i][j] = ' '  # Прохідна зона
        return maze

    def generate_food(self):
        # Генерація їжі на порожніх місцях лабіринту
        food_positions = []
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if self.maze[y][x] == ' ':
                    food_positions.append((x, y))
        return food_positions

    def draw(self, screen):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == '#':
                    pygame.draw.rect(screen, (255, 255, 255), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif (x, y) in self.food_positions:
                    screen.blit(self.food_icon, (x * CELL_SIZE, y * CELL_SIZE))
