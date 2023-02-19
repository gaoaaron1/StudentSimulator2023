import pygame
from config import *

class Term:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font('junegull.ttf', 24)

    def draw(self):

        # Draw the HUD label on the screen
        self.game.screen.blit(self.text, self.rect)  
           

class Timer(pygame.sprite.Sprite):
    def __init__(self, game, time):
        super().__init__()
        self.game = game
        self.time = time  # time in milliseconds
        self.start_time = pygame.time.get_ticks()
        self.font = pygame.font.Font('junegull.ttf', 32)

    def update(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        self.time = max(0, self.time - elapsed_time)
        self.start_time = pygame.time.get_ticks()
        if self.time == 0:
            self.game.playing = False

    def draw(self):
        # Convert time from milliseconds to minutes and seconds
        seconds = self.time // 1000
        minutes = seconds // 60
        seconds %= 60

        # Create text surface with the time in the format of "mm:ss"
        time_text = f"{minutes:02d}:{seconds:02d}"
        text_surface = self.font.render(time_text, True, WHITE)

        # Blit the text surface onto the screen
        self.game.screen.blit(text_surface, (10, 10))