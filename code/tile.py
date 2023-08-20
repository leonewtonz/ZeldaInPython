# At the beginning, it's always a rock.
# But later on, it will become more flexiable: tree, obstacle...

import pygame
from settings import *
import os


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        # ../ mean to go up one directory. Currently in /code
        self.image = pygame.image.load("../graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)