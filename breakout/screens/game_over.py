import pygame
from screens import BaseScreen
from components import TextBox


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.button1 = TextBox(
            (200, 100), "Again", color=(255, 0, 0), bgcolor=(120, 120, 120)
        )
        self.button2 = TextBox(
            (200, 100), "Quit", color=(0, 255, 0), bgcolor=(255, 140, 70)
        )
        self.message = TextBox(
            (400, 200), "You Lost!", color=(255, 0, 0), bgcolor=(150, 40, 140)
        )
        self.button1.rect.topleft = (100, 550)
        self.button2.rect.topleft = (500, 550)
        self.message.rect.topleft = (200, 250)
        self.sprites.add(self.button1, self.button2, self.message)
        

    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
