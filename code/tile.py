# At the beginning, it's always a rock.
# But later on, it will become more flexiable: tree, obstacle...

import pygame
from settings import *
import os


class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        # ../ mean to go up one directory. Currently in /code
        path = os.getcwd()
        print(path)
        rock = os.path.join(path, "graphics/test", "rock.png")
        self.image = pygame.image.load(rock).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)