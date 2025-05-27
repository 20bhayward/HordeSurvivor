import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FIREBRICK, ENEMY_SPEED # Changed ENEMY_COLOR to FIREBRICK
from player import Player 

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(FIREBRICK) # Use FIREBRICK
        # TODO: Load enemy sprite e.g., self.image = pygame.image.load('assets/sprites/enemies/epoch1/primordial_grunt.png').convert_alpha()
        self.rect = self.image.get_rect()
        # Spawn at a random position
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

    def update(self, player: Player):
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        dist = (dx**2 + dy**2)**0.5

        if dist > 0:
            dx /= dist
            dy /= dist

        self.rect.x += dx * ENEMY_SPEED
        self.rect.y += dy * ENEMY_SPEED
