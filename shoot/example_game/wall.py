import pygame_ai as pai
import pygame

class Wall(pai.gameobject.GameObject):
    """ Class to represent walls in the game """
    def __init__(self, pos, dims, color = (47, 79, 79)):
        image = pygame.Surface(dims).convert()
        image.fill(color)
        pygame.draw.rect(image, (0, 0, 0), image.get_rect(), 2)
        super(Wall, self).__init__(image, max_accel = 0, max_angular_accel = 0)
        self.rect.topleft = pos
        
    def get_lines(self):
        left = [self.rect.topleft, self.rect.bottomleft]
        top = [self.rect.topleft, self.rect.topright]
        right = [self.rect.topright, self.rect.bottomright]
        bottom = [self.rect.bottomright, self.rect.bottomleft]
        
        return [left, top, right, bottom]
