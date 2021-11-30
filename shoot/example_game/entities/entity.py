import pygame

import pygame_ai as pai
import globs

def is_colliding(sprite, group):
    for sprite2 in group:
        if sprite != sprite2 and pygame.sprite.collide_rect(sprite, sprite2):
            return True
    
    return False

class Entity(pai.gameobject.GameObject):
    
    def __init__(self, img_surf, pos = (0, 0), max_speed = 40, max_accel = 20, max_rotation = 30, max_angular_accel = 20):
        super(Entity, self).__init__(img_surf, pos, max_speed, max_accel, max_rotation, max_angular_accel)
        self.external_forces = dict()
        self.on_ground = False
        
    def update(self, steering, tick):
        # Apply steering and gravity
        self.steer(steering, tick)
        
        # Move and check for collision
        self.move_with_collision(tick)
        
        # Apply drag
        self.steer(globs.drag.get_steering(self), tick)
        
    def move_without_collision(self, tick):
        self.rect.move_ip(self.velocity * tick)
        
        self.orientation += self.rotation
        self.orientation %= 360
        self.image = pygame.transform.rotate(self.original_image, int(self.orientation))
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
        
        
    def move_with_collision(self, tick):
        velocity = self.velocity + self.get_external_velocities()
        
        dx = velocity[0]*tick
        dy = velocity[1]*tick
        
        self.rect.move_ip(dx, 0)
        if is_colliding(self, globs.solid_entities):
            self.rect.move_ip(-dx, 0)
            
        self.rect.move_ip(0, dy)
        if is_colliding(self, globs.solid_entities):
            self.on_ground = True
            self.rect.move_ip(0, -dy)
        else:
            self.on_ground = False
            
        self.orientation += self.rotation
        self.orientation %= 360
        self.image = pygame.transform.rotate(self.original_image, int(self.orientation))
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center
            
    def get_external_velocities(self):
        velocity = pygame.Vector2(0, 0)
        for force in self.external_forces.values():
            velocity += force.linear
            
        return velocity
            
