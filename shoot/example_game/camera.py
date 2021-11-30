""" Sorry, no docs for this """

import pygame

class Camera(object):
    
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        return entity.rect.move(self.state.topleft)
        
    def apply_rect(self, rect):
        return rect.move(self.state.topleft)
        
    def apply_norect(self, pos):
        offset = self.state.topleft
        return pygame.Vector2(pos[0] + offset[0], pos[1] + offset[1])
        
    def update(self, entity):
        self.state = self.camera_func(self.state, entity.rect)
        
def simple_camera(screen_width, screen_height, cam, entity_rect):
    l, t, _, _ = entity_rect
    _, _, w, h = cam
    
    return pygame.Rect(-l+screen_width/2, -t+screen_height/2, w, h)
    
def complex_camera(screen_width, screen_height, camera, target_rect):
    x = -target_rect.center[0] + screen_width/2 
    y = -target_rect.center[1] + screen_height/2
    camera.topleft += (pygame.Vector2((x, y)) - pygame.Vector2(camera.topleft)) * 0.06
    camera.x = max(-(camera.width-screen_width), min(0, camera.x))
    camera.y = max(-(camera.height-screen_height), min(0, camera.y))
    
    return camera
