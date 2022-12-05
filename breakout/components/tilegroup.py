import pygame
from .tile import Tile


class TileGroup(pygame.sprite.Group):
    def __init__(self, tile_width=100, tile_height=30):
        super().__init__()

        tile = Tile(width=tile_width, height=tile_height)

        tile.move_to(400, 400)
        self.add(tile)
