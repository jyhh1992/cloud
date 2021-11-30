import pygame
import pygame_ai as pai
import pygame_ai.utils.math_utils as math_utils

import colors
from entities.entity import Entity
import globs

class Player(Entity):
    """ Holds the logic for the player """
    
    def __init__(self, radius = 7, pos = (0, 0), color = colors.BLUE):
        color = (color[0], color[1], color[2], 255)
        darker_color = colors.get_darker(color)
        img = pygame.Surface((radius*2, radius*2)).convert_alpha()
        img.fill((255, 255, 255, 0))
        pygame.draw.circle(img, color, (radius, radius), radius)
        pygame.draw.circle(img, darker_color, (radius, radius), radius, 1)
        super(Player, self).__init__(img, pos)
        self.jumping = False
        self.on_ground = True
        
    def jump(self):
        pass


class PlayerGravity(Entity):
    """ Holds the logic for the player """
    
    def __init__(self, size = (10, 15), pos = (0, 0), color = colors.BLUE):
        img = pygame.Surface(size).convert()
        img.fill(color)
        darker_color = colors.get_darker(color)
        pygame.draw.rect(img, darker_color, img.get_rect(), 1)
        super(PlayerGravity, self).__init__(img, pos)
        # Gravity
        self.external_forces['gravity'] = globs.gravity
        
        self.jump_steering = pai.steering.kinematic.SteeringOutput()
        self.jump_steering.linear[1] = -globs.gravity.linear[1]*3
        self.jump_counter = 10
        self.jumping = False
        self.on_ground = True
        
    def jump(self):
        if not self.jumping and self.on_ground:
            self.jump_counter = 0
            self.jumping = True
            self.external_forces['jump'] = self.jump_steering
        
    def update(self, steering, tick):
        # Apply steering along x
        self.steer_x(steering, tick)
        
        # Jump mechanics
        if self.jumping:
            self.jump_counter += 1
            
        if self.jumping and self.jump_counter > 10:
            del self.external_forces['jump']
            self.jumping = False
        
        # Move and check for collision
        self.move_with_collision(tick)
        
        # Apply drag
        self.steer(globs.drag.get_steering(self), tick)
        
