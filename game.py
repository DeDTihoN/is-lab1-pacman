import time

import pygame
from pacman import Pacman, Direction
from ghost import Ghost
from level import Level
from settings import WIDTH, HEIGHT, FPS

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def main():
    level = Level(1)
    pacman = Pacman(1, 1, level.pacman_speed, 'play')
    ghosts = [Ghost(g['x'], g['y'], level.ghost_speed, g['behavior'], g['icon']) for g in level.ghosts]

    running = True
    last_pressed = Direction(0, 1)
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            last_pressed = Direction(-1, 0)
        elif keys[pygame.K_RIGHT]:
            last_pressed = Direction(1, 0)
        elif keys[pygame.K_UP]:
            last_pressed = Direction(0, -1)
        elif keys[pygame.K_DOWN]:
            last_pressed = Direction(0, 1)

        level.maze.draw(screen)
        pacman.draw(level.maze.maze, screen)

        for ghost in ghosts:
            ghost.draw(level.maze.maze, screen)

        for ghost in ghosts:
            ghost.move(pacman, level.maze.maze)

        pacman.move(level.maze.maze, last_pressed)
        if level.is_food_collected():
            level.next_level()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
