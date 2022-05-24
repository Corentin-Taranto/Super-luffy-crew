import pygame

from pygame.time import Clock

from constants.view import *
from constants.images import *
from view.ground import Ground

pygame.init()

class Game:
    def __init__(self):
        # Create window
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.is_window_closed = False
        self.clock = Clock()
        self.ground = Ground(self.window)

    def draw_background(self):
        # self.window.blit(BACKGROUND_IMG, (0, 0))
        pass

    def poll_events(self):
        while not self.is_window_closed:
            pygame.display.update()
            self.clock.tick(30)
            self.draw_background()
            self.ground.draw_ground()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.is_window_closed = True
