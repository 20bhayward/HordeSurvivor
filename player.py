import pygame
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, ANTIQUE_WHITE, PLAYER_SPEED, # Changed WHITE to ANTIQUE_WHITE
                    XP_PER_LEVEL, LEVEL_UP_HEALTH_INCREASE, 
                    LEVEL_UP_SPEED_INCREASE, LEVEL_UP_DAMAGE_INCREASE)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(ANTIQUE_WHITE) # Use ANTIQUE_WHITE
        # TODO: Load player sprite e.g., self.image = pygame.image.load('assets/sprites/player/player_epoch1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        
        self.xp = 0
        self.last_attack_time = 0
        
        self.level = 1
        self.max_health = 100
        self.current_health = self.max_health
        self.speed = PLAYER_SPEED 
        self.damage = 5 
        self.xp_to_next_level = XP_PER_LEVEL

    def level_up(self):
        self.level += 1
        self.max_health += LEVEL_UP_HEALTH_INCREASE
        self.current_health = self.max_health # Full heal
        self.speed += LEVEL_UP_SPEED_INCREASE
        self.damage += LEVEL_UP_DAMAGE_INCREASE
        # self.xp = 0 # Reset XP for the new level or carry over excess
        # self.xp -= self.xp_to_next_level # Handled in game.py with excess_xp
        self.xp_to_next_level = int(self.xp_to_next_level * 1.5)
        
        print(f"Player leveled up to Level {self.level}!")
        print(f"Max Health: {self.max_health}, Speed: {self.speed:.2f}, Damage: {self.damage}")
        print(f"XP for next level: {self.xp_to_next_level}")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed # Use self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed # Use self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed # Use self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed # Use self.speed

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
