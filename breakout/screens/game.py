import random
import pygame
import time
from screens import BaseScreen

from ..components import Paddle, Ball, TileGroup
from components import TextBox

global start_time, end_time

class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the paddle
        self.paddle = Paddle(200, 30, (0, 255, 0), limits=self.rect)

        # Create the ball
        self.ball = Ball(limits=self.rect)
        self.ball.speed = 8

        self.ball.angle = random.randint(0, 31416) / 10000

        # Create the tiles
        self.tiles = TileGroup(tile_width=120, tile_height=30)

        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.paddle)
        self.sprites.add(self.ball)
        
        # Record score and level
        self.score = 0
        self.level = 1

        start_time = time.time()

    def update(self):
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

        self.sprites.update()
        collided = self.ball.collidetiles(self.tiles)

        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)

        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            self.running = False
            self.next_screen = "game_over"
            end_time = time.time()
            self.score = self.count_score(start_time, end_time, self.level)
        
        if not self.tiles:
            self.level += 1
            if self.level <= 3:
                self.tiles = TileGroup(self.level, tile_width=120, tile_height=30)
                self.tiles.update()
            self.running = False
            self.next_screen = "game_over"
            end_time = time.time()
            self.score = self.count_score(start_time, end_time, self.level)

    def count_score(self, start, end, level):
        total = end - start
        score = 45*level/total

        return int(score) 



    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = 1.5
