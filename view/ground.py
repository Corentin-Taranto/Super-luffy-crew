from pygame import Surface

from constants.images import GROUND_IMG

class Ground:
    def __init__(self, window: Surface):
        self.window = window

    def draw_ground(self):
        for i in range(0, 100):
            self.window.blit(GROUND_IMG, (i * 32, 568))