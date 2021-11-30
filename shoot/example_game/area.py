import pygame

import globs

class Area(object):
    
    def __init__(self, x, color):
        self.x = x
        self.rect = pygame.Rect(x, globs.tilesize, globs.area_width, globs.screen_height - globs.tilesize*2)
        pygame.draw.rect(globs.background, color, self.rect, 1)
        self.entities = []
        self.entry_actions = []
        self.exit_actions = []
