import pygame
from config import WEAPON_COLOR, WEAPON_SIZE, WEAPON_DURATION

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        super().__init__()
        self.image = pygame.Surface(WEAPON_SIZE)
        self.image.fill(WEAPON_COLOR)
        self.image.set_alpha(128) # Semi-transparent
        self.rect = self.image.get_rect(center=player_rect.center)
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        if pygame.time.get_ticks() - self.spawn_time > WEAPON_DURATION:
            self.kill() # Remove sprite after duration
