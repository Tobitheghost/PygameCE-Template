from state.state import State
from game.settings import *

import pygame

class Clicker(State):
    def __init__(self, game):
        State.__init__(self, game, "Clicker")
        self.screen = pygame.display.get_surface()
        self.color = "Blue"
    
    def get_event(self, event:pygame.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.color = "Red"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.color = "Blue"
    
    def update(self, dt):
        super().update(dt)

    def draw(self):
        self.screen.fill(self.color)