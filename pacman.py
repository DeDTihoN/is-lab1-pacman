import random

import pygame

from settings import PACMAN_ICON, CELL_SIZE


class Direction:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Pacman:
    def __init__(self, x, y, speed, behavior):
        self.x = x
        self.y = y
        self.speed = speed
        self.icon = pygame.image.load(PACMAN_ICON).convert_alpha()
        self.rect = self.icon.get_rect()
        self.direction = Direction(0, 0)
        self.status = 0
        self.behavior = behavior

    def move(self, maze, last_pressed):
        self.status += self.speed
        if self.status >= 1:
            self.status = 0
            if maze[self.y + self.direction.x][self.x + self.direction.y] != '#':
                self.x += self.direction.x
                self.y += self.direction.y
            self.change_direction(maze, last_pressed)

    def change_direction(self, maze, last_pressed):
        if self.behavior == 'play':
            self.direction = last_pressed
        elif self.behavior == 'auto':
            possible_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            available_directions = []
            for direction in possible_directions:
                if maze[self.y + direction[0]][self.x + direction[1]] != '#':
                    available_directions.append(direction)
            if len(available_directions) > 0:
                self.direction = random.choice(available_directions)

    def draw(self, maze, screen):
        if maze[self.y + self.direction.x][self.x + self.direction.y] != '#':
            screen.blit(self.icon, ((self.x + self.direction.x * self.status) * CELL_SIZE,
                                    (self.y + self.direction.y * self.status) * CELL_SIZE))
        else:
            screen.blit(self.icon, (self.x * CELL_SIZE, self.y * CELL_SIZE))
