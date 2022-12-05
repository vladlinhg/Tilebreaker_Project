import pygame

from .sprite import MySprite


class Paddle(MySprite):
    """Represents the game paddle"""

    def __init__(self, width, height, color=(0, 0, 0), **kwargs):
        super().__init__(**kwargs)
        self.original_image = pygame.image.load("breakout/components/img/paddle.png")
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()

        if self.limits:
            self.move_to(
                self.limits.center[0] - self.rect.width / 2,
                self.limits.bottom - self.rect.height,
            )
