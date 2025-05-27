import pygame
from enemy import Enemy
from xp_orb import XPOrb # Import XPOrb
from config import ENEMY_SPAWN_RATE, MAX_ENEMIES

class Game:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.xp_orbs = pygame.sprite.Group() # Add xp_orbs group
        self.active_weapons = pygame.sprite.Group() # Add active_weapons group
        self.player = None # To be set later
        self.last_spawn_time = pygame.time.get_ticks()
        self.wave_number = 1 # Optional, for future use

    def set_player(self, player):
        self.player = player
        self.all_sprites.add(self.player)

    def spawn_enemy(self):
        if len(self.enemies) < MAX_ENEMIES:
            new_enemy = Enemy()
            self.all_sprites.add(new_enemy)
            self.enemies.add(new_enemy)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > ENEMY_SPAWN_RATE:
            self.spawn_enemy()
            self.last_spawn_time = current_time
        
        self.active_weapons.update() # Update active weapons
        self.handle_attacks()
        self.handle_xp_collection()

    def handle_attacks(self):
        for weapon in self.active_weapons:
            hit_enemies = pygame.sprite.spritecollide(weapon, self.enemies, True) # True to kill enemies
            for enemy in hit_enemies:
                new_orb = XPOrb(enemy.rect.centerx, enemy.rect.centery)
                self.xp_orbs.add(new_orb)
                self.all_sprites.add(new_orb) # Add to all_sprites for drawing

    def handle_xp_collection(self):
        collected_orbs = pygame.sprite.spritecollide(self.player, self.xp_orbs, True) # True to kill orbs
        for orb in collected_orbs:
            self.player.xp += orb.xp_value
            print(f"Player XP: {self.player.xp}/{self.player.xp_to_next_level}") # For debugging
            if self.player.xp >= self.player.xp_to_next_level:
                excess_xp = self.player.xp - self.player.xp_to_next_level
                self.player.level_up()
                self.player.xp = excess_xp
                # Check for multiple level ups if excess_xp is still high, though less likely with scaling
                while self.player.xp >= self.player.xp_to_next_level:
                    excess_xp = self.player.xp - self.player.xp_to_next_level
                    self.player.level_up()
                    self.player.xp = excess_xp
