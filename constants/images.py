import pygame
import os

from constants.view import *

BACKGROUND_IMG = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "Background.png")), (WINDOW_WIDTH, WINDOW_HEIGHT)
)

GROUND_IMG = pygame.image.load(os.path.join("assets", "Ground2.png"))