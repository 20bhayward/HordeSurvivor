import pygame
import sys # Import sys
from player import Player
from game import Game
from weapon import Weapon
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, DARK_SLATE_GRAY,
                    ATTACK_COOLDOWN, EPOCH_NAME, LORE_TEXT_COLOR, FPS) # Import FPS

pygame.init() # Pygame initialization
pygame.font.init() # Explicitly initialize font module (good practice)
# pygame.mixer.init() # Optional: For sound later

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(EPOCH_NAME) # Use Epoch name for window title

# Font for lore text
pygame.font.init() # Ensure font module is initialized
lore_font = pygame.font.SysFont('Arial', 24) # Or a more thematic font if available
from config import (UI_FONT_SIZE, UI_FONT_COLOR, UI_XP_BAR_COLOR, UI_HEALTH_BAR_COLOR,
                    UI_BAR_HEIGHT, UI_BAR_WIDTH) # Import UI settings
ui_font = pygame.font.SysFont('Arial', UI_FONT_SIZE)


# Create Game instance
game = Game()

# Create Player instance
player = Player()

# Set player in the game object
game.set_player(player)

# Old direct enemy and sprite group creation (remove or comment out)
# enemy = Enemy()
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)
# all_sprites.add(enemy)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input for attacks
    keys = pygame.key.get_pressed()
    now = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and now - player.last_attack_time > ATTACK_COOLDOWN:
        player.last_attack_time = now
        new_weapon = Weapon(player.rect)
        game.all_sprites.add(new_weapon)
        game.active_weapons.add(new_weapon)

    player.update() # Handle player input and movement
    game.update()   # Handle enemy spawning, weapon updates, attacks, XP collection

    # Update all enemies in the game's enemy group, passing the player for targeting
    game.enemies.update(player)

    screen.fill(DARK_SLATE_GRAY) # Use new background color
    
    # Display Epoch Name (Lore)
    lore_surface = lore_font.render(EPOCH_NAME, True, LORE_TEXT_COLOR)
    screen.blit(lore_surface, (10, 10))

    # Display Player Level
    level_text = f"Level: {player.level}"
    level_surface = ui_font.render(level_text, True, UI_FONT_COLOR)
    screen.blit(level_surface, (10, 40))

    # Display Player Health
    health_text = f"HP: {player.current_health} / {player.max_health}"
    health_surface = ui_font.render(health_text, True, UI_FONT_COLOR)
    screen.blit(health_surface, (10, 65))
    # Health Bar
    health_ratio = player.current_health / player.max_health if player.max_health > 0 else 0
    health_bar_current_width = int(UI_BAR_WIDTH * health_ratio)
    health_bar_bg_rect = pygame.Rect(10, 90, UI_BAR_WIDTH, UI_BAR_HEIGHT)
    pygame.draw.rect(screen, (50,50,50), health_bar_bg_rect) # Draw background first
    health_bar_rect = pygame.Rect(10, 90, health_bar_current_width, UI_BAR_HEIGHT)
    pygame.draw.rect(screen, UI_HEALTH_BAR_COLOR, health_bar_rect)
    pygame.draw.rect(screen, (50,50,50), health_bar_bg_rect, 2) # Draw border on top

    # Display Player XP
    xp_text = f"XP: {player.xp} / {player.xp_to_next_level}"
    xp_surface = ui_font.render(xp_text, True, UI_FONT_COLOR)
    screen.blit(xp_surface, (10, 115))
    # XP Bar
    xp_ratio = player.xp / player.xp_to_next_level if player.xp_to_next_level > 0 else 0
    xp_bar_current_width = int(UI_BAR_WIDTH * xp_ratio)
    xp_bar_bg_rect = pygame.Rect(10, 140, UI_BAR_WIDTH, UI_BAR_HEIGHT)
    pygame.draw.rect(screen, (50,50,50), xp_bar_bg_rect) # Draw background first
    xp_bar_rect = pygame.Rect(10, 140, xp_bar_current_width, UI_BAR_HEIGHT)
    pygame.draw.rect(screen, UI_XP_BAR_COLOR, xp_bar_rect)
    pygame.draw.rect(screen, (50,50,50), xp_bar_bg_rect, 2) # Draw border on top

    # Display Wave Number
    wave_text = f"Wave: {game.wave_number}"
    wave_surface = ui_font.render(wave_text, True, UI_FONT_COLOR)
    wave_rect = wave_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    screen.blit(wave_surface, wave_rect)
    
    game.all_sprites.draw(screen) # Draw all sprites (player and enemies) managed by game

    pygame.display.flip()
    clock.tick(FPS) # Use FPS from config

pygame.quit()
sys.exit() # Ensure clean exit
