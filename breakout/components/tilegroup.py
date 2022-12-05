import pygame
import json
from .tile import Tile



class TileGroup(pygame.sprite.Group):
    def __init__(self,  level=1, tile_width=100, tile_height=30):
        super().__init__()

        filename = "level_" + str(level) +".json"

        input_file = open ("breakout/components/level/" + filename)
        tile_array = json.load(input_file)

        self.number = 0

        for placement in tile_array:
            tile = Tile(width=tile_width, height=tile_height)
            tile.move_to(placement["x"], placement["y"])
            self.add(tile)
            self.number += 1

        
