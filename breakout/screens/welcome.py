import pygame
from screens import BaseScreen
from components import TextBox


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button = TextBox(
            (200, 100), "Press SPACE", color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.sprites.add(self.button)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.button.rect.x = 200
        self.button.rect.y = 400
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
