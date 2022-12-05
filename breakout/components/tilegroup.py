import pygame
import json
from .tile import Tile



class TileGroup(pygame.sprite.Group):
    def __init__(self, tile_width=100, tile_height=30, level=1):
        super().__init__()

        filename = "level_" + str(level) +".json"

        input_file = open ("breakout/components/level/" + filename)
        tile_array = json.load(input_file)

        for placement in tile_array:
            tile = Tile(width=tile_width, height=tile_height)
            tile.move_to(placement["x"], placement["y"])
            self.add(tile)

        
