from state.state import State
from game.settings import *

import pygame

class Main_Menu(State):
    def __init__(self, game):
        State.__init__(self, game, "Main_Menu")
        self.screen = pygame.display.get_surface()
        
        self.list_of_keys = list(self.game.states.keys())
        rect = self.screen.get_height
        title_offset = 32
        self.list_of_screens = []
        self.list_of_rects = []
        for text in self.list_of_keys:
            title = (self.font_text.render(text, False, WHITE))
            self.list_of_screens.append(title)
            self.list_of_rects.append(title.get_rect(topleft=(self.screen_rect.topleft[0] + 32, self.screen_rect.topleft[1] + title_offset)))
            title_offset += 32
    
    def get_event(self, event:pygame.Event):
        for id, rect in enumerate(self.list_of_rects):
            if rect.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.next_state = self.list_of_keys[id]
                    self.done = True
                    
    
    def update(self, dt):
        ...

    def draw(self):
        self.screen.fill(BLACK)
        for id, title in enumerate(self.list_of_screens):
            self.screen.blit(title,self.list_of_rects[id])
