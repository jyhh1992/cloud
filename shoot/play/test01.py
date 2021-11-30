import sys

import pygame
from pygame.locals import *
import pygame_ai as pai

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Custom classes and definitions
# ...

def main():

    # Create screen
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('PyGame AI Guide')

    # Create white background
    background = pygame.Surface((screen_width, screen_height)).convert()
    background.fill((255, 255, 255))

    # Initialize clock
    clock = pygame.time.Clock()

    # Variables that you will use in your game loop
    # ...

    # Game loop
    while True:

        # Get loop time, convert milliseconds to seconds
        tick = clock.tick(60)/1000

        # Handle input
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(2)

        # Erase previous frame by bliting background
        screen.blit(background, background.get_rect())

        # Update the entities in your game
        # ...

        # Blit all your entities
        # . . .

        # Update display
        pygame.display.update()





if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()