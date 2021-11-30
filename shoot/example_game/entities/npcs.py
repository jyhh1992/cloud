import pygame
import pygame_ai as pai

import colors
from entities.entity import Entity
import globs

class Rectangle(Entity):
    
    def __init__(self, size = (10, 15), pos = (0, 0), color = colors.RED):
        # Create rectangle image
        img = pygame.Surface(size).convert()
        img.fill(color)
        darker_color = colors.get_darker(color)
        pygame.draw.rect(img, darker_color, img.get_rect(), 1)
        rect = img.get_rect()
        rect.left = rect.right - rect.width//3
        pygame.draw.rect(img, darker_color, rect)
        
        # Initialize entity
        super(Rectangle, self).__init__(img, pos)
        
        # Assign placeholder ai
        self.ai = pai.steering.kinematic.NullSteering()
        
        # Make it affected by gravity
        #self.external_forces.append(globs.gravity)
        self.external_forces['gravity'] = globs.gravity
        self.jump_steering = pai.steering.kinematic.SteeringOutput()
        self.jump_steering.linear[1] = -globs.gravity.linear[1]*2
        self.jump_counter = 10
        self.jumping = False
        self.on_ground = True
        self.jump_treshold = 5
        
    def jump(self):
        if not self.jumping and self.on_ground:
            self.jump_counter = 0
            self.jumping = True
            self.external_forces['jump'] = self.jump_steering
    
    def update(self, tick):
        steering = self.ai.get_steering()
        # Apply steering along x
        self.steer_x(steering, tick)
        # Decide where to face
        if steering.linear[0] >= 0:
            self.orientation = 0
        else:
            self.orientation = 180

        if abs(steering.linear[1]) > self.jump_treshold:
            self.jump()
        
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
        
class Triangle(Entity):
    
    def __init__(self, base = 15, height = 15, pos = (0, 0), color = colors.PURPLE, max_speed = 35, max_accel = 20, max_rotation = 30, max_angular_accel = 20):
        # Create triangle image
        color = (color[0], color[1], color[2], 255)
        darker_color = colors.get_darker(color)
        img = pygame.Surface((height, base)).convert_alpha()
        img.fill((255, 255, 255, 0))
        points = [(0,0), (height, base//2), (0, base)]
        pygame.draw.polygon(img, color, points)
        pygame.draw.polygon(img, darker_color, points, 1)
        points = points = [(height//2, base//4), (height, base//2), (height//2, base-base//4)]
        pygame.draw.polygon(img, darker_color, points)
        
        # Initialize entiy
        super(Triangle, self).__init__(img, pos, max_speed = max_speed, max_accel = max_accel)
        
        # Asign placeholder ai
        self.ai = pai.steering.kinematic.NullSteering()
        
    def update(self, tick):
         # Apply AI steering
        steering = self.ai.get_steering()
        #self.ai.draw_indicators(globs.screen, globs.cam.apply_norect)
        super(Triangle, self).update(steering, tick)
        

class Circle(Entity):
    
    def __init__(self, radius = 5, pos = (0, 0), color = colors.RED, max_speed = 35, max_accel = 25):
        # Create circle image
        color = (color[0], color[1], color[2], 255)
        darker_color = colors.get_darker(color)
        img = pygame.Surface((radius*2, radius*2)).convert_alpha()
        img.fill((255, 255, 255, 0))
        pygame.draw.circle(img, color, (radius, radius), radius)
        pygame.draw.circle(img, darker_color, (radius, radius), radius, 1)
        
        # Initialize entity
        super(Circle, self).__init__(img, pos, max_speed = max_speed, max_accel = max_accel)
        
        # Placeholder AI
        self.ai = pai.steering.kinematic.NullSteering()
        
    def update(self, tick):
        steering = self.ai.get_steering()
        #self.ai.draw_indicators(globs.screen, globs.cam.apply_norect)
        super(Circle, self).update(steering, tick)
        
class NotSolidCircle(Entity):
    
    def __init__(self, radius = 2, pos = (0, 0), color = colors.RED):
        # Create circle image
        color = (color[0], color[1], color[2], 255)
        darker_color = colors.get_darker(color)
        img = pygame.Surface((radius*2, radius*2)).convert_alpha()
        img.fill((255, 255, 255, 0))
        pygame.draw.circle(img, color, (radius, radius), radius)
        pygame.draw.circle(img, darker_color, (radius, radius), radius, 1)
        
        # Initialize entity
        super(NotSolidCircle, self).__init__(img, pos, max_speed = 55, max_accel = 30)
        
        # Placeholder AI
        self.ai = pai.steering.kinematic.NullSteering()
        
    def update(self, tick):
        steering = self.ai.get_steering()
        
        # Apply steering and gravity
        self.steer(steering, tick)
        
        # Move and check for collision
        self.move_without_collision(tick)
        
        
