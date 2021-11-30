import os
import pygame
from globs import gvars

def load_image(img_name):
    """ Load image and return in a surface and it's rect """
    fullname = os.path.join(gvars.IMG_FOLDER, img_name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        
    except pygame.error as message:
        raise SystemExit(message)
        
    #return image, image.get_rect()
    return image
