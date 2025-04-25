from state.state import State
from game.settings import *

import pygame

class Parallax(State):
    def __init__(self, game):
        State.__init__(self, game, "Parallax")
        self.screen = pygame.display.get_surface()
        background_layer_1 = pygame.image.load("screens\\parallax\\images\\background-layer-1.png").convert_alpha()
        background_layer_2 = pygame.image.load("screens\\parallax\\images\\background-layer-2.png").convert_alpha()
        background_layer_3 = pygame.image.load("screens\\parallax\\images\\background-layer-3.png").convert_alpha()
        
        self.bg_surf1 = pygame.Surface((background_layer_1.get_rect().width * 3, background_layer_1.get_rect().height))
        self.bg_surf1.set_colorkey((0,0,0))
        self.bg_surf1.blits(blit_sequence=((background_layer_1,(-1 * background_layer_1.get_rect().width,0)),
                            (background_layer_1,(0,0)),
                            (background_layer_1,(background_layer_1.get_rect().width,0))))
        
        self.bg_surf2 = pygame.Surface((background_layer_2.get_rect().width * 3, background_layer_2.get_rect().height))
        self.bg_surf2.set_colorkey((0,0,0))
        self.bg_surf2.blits(blit_sequence=((background_layer_2,(-1 * background_layer_2.get_rect().width,0)),
                            (background_layer_2,(0,0)),
                            (background_layer_2,(background_layer_2.get_rect().width,0))))
        
        self.bg_surf3 = pygame.Surface((background_layer_3.get_rect().width * 3, background_layer_3.get_rect().height))
        self.bg_surf3.set_colorkey((0,0,0))
        self.bg_surf3.blits(blit_sequence=((background_layer_3,(-1 * background_layer_3.get_rect().width,0)),
                            (background_layer_3,(0,0)),
                            (background_layer_3,(background_layer_3.get_rect().width,0))))

        self.scroll = 0
        
    def get_event(self, event:pygame.Event):
        ...
    
    def get_background_x(self, scroll_mod):
        scroll_offset = self.scroll * scroll_mod
        bg_offset = int(scroll_offset / pygame.display.get_window_size()[0]) * pygame.display.get_window_size()[0]
        return scroll_offset - bg_offset
    
    def update(self, dt):
        super().update(dt)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            direction = 1
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            direction = -1
        else:
            direction = 0
        
        self.scroll += direction

    def draw(self):
        self.screen.fill(PURPLE)
        self.screen.blit(self.bg_surf3, (self.get_background_x(.01) - SCREEN_WIDTH,0))
        self.screen.blit(self.bg_surf2, (self.get_background_x(.02) - SCREEN_WIDTH,0))
        self.screen.blit(self.bg_surf1, (self.get_background_x(.03) - SCREEN_WIDTH,0))