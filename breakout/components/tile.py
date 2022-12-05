import pygame
from .sprite import MySprite
import random


class Tile(MySprite):
    """Tile - meant to be hit with the ball"""

    def __init__(self, *args, width=100, height=30, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_image = pygame.image.load("breakout/components/img/tile.jpg")
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()
