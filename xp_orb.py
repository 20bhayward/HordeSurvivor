import pygame
from config import XP_ORB_COLOR, XP_ORB_SIZE

class XPOrb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(XP_ORB_SIZE)
        self.image.fill(XP_ORB_COLOR)
        self.rect = self.image.get_rect(center=(x, y))
        self.xp_value = 10
