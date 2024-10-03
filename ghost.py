import pygame
import random

from pacman import Direction
from settings import CELL_SIZE, GHOST1_ICON, GHOST2_ICON


class Ghost:
    def __init__(self, x, y, speed, behavior, icon_path):
        self.x = x
        self.y = y
        self.speed = speed
        self.behavior = behavior
        self.icon = pygame.image.load(icon_path).convert_alpha()
        self.direction = Direction(0, 0)
        self.status = 0

    def move(self, pacman, maze):
        self.status += self.speed
        if self.behavior == 'x_first':
            self.move_x_first(pacman, maze)
        elif self.behavior == 'y_first':
            self.move_y_first(pacman, maze)

    def move_x_first(self, pacman, maze):
        if self.status >= 1:
            if self.check_direction(maze, self.direction):
                self.x += self.direction.x
                self.y += self.direction.y
            self.status = 0
            wanted_direction = None
            if pacman.x != self.x:
                if pacman.x > self.x:
                    wanted_direction = Direction(1, 0)
                else:
                    wanted_direction = Direction(-1, 0)
            if wanted_direction is not None and self.check_direction(maze, wanted_direction):
                self.direction = wanted_direction
                return
            possible_directions = [Direction(1, 0), Direction(-1, 0), Direction(0, 1), Direction(0, -1)]
            filter(lambda pos_direction: self.check_direction(maze, pos_direction), possible_directions)

            if len(possible_directions) > 0:
                best_direction = possible_directions[0]
                for direction in possible_directions:
                    if abs(pacman.x - (self.x + direction.x)) + abs(pacman.y - (self.y + direction.y)) < abs(
                            pacman.x - (self.x + best_direction.x)) + abs(pacman.y - (self.y + best_direction.y)):
                        best_direction = direction
                self.direction = best_direction

    def move_y_first(self, pacman, maze):
        if self.status >= 1:
            if self.check_direction(maze, self.direction):
                self.x += self.direction.x
                self.y += self.direction.y
            self.status = 0
            wanted_direction = None
            if pacman.y != self.y:
                if pacman.y > self.y:
                    wanted_direction = Direction(0, 1)
                else:
                    wanted_direction = Direction(0, -1)
            if wanted_direction is not None and self.check_direction(maze, wanted_direction):
                self.direction = wanted_direction
                return
            possible_directions = [Direction(1, 0), Direction(-1, 0), Direction(0, 1), Direction(0, -1)]
            filter(lambda pos_direction: self.check_direction(maze, pos_direction), possible_directions)

            if len(possible_directions) > 0:
                best_direction = possible_directions[0]
                for direction in possible_directions:
                    if abs(pacman.x - (self.x + direction.x)) + abs(pacman.y - (self.y + direction.y)) < abs(
                            pacman.x - (self.x + best_direction.x)) + abs(pacman.y - (self.y + best_direction.y)):
                        best_direction = direction
                self.direction = best_direction

    def check_direction(self, maze, cur_direction):
        if maze[self.y + cur_direction.y][self.x + cur_direction.x] != '#':
            return True
        return False

    def draw(self, maze, screen):
        if self.check_direction(maze, self.direction):
            screen.blit(self.icon, ((self.x + self.direction.x * self.status) * CELL_SIZE,
                                    (self.y + self.direction.y * self.status) * CELL_SIZE))
        else:
            screen.blit(self.icon, (self.x * CELL_SIZE, self.y * CELL_SIZE))
