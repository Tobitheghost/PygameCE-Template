from game.settings import *
from state.state import State
import pygame

class SplashScreen(State):
    def __init__(self, game) -> None:
        State.__init__(self, game, "SplashScreen")
        
        self.time = 0
        self.end_time = 2
        self.color = BLACK
        
        self.splash_screen = pygame.Surface((SCREEN_WIDTH * SCREEN_SCALE, SCREEN_HEIGHT * SCREEN_SCALE))

        self.title = self.font_title.render("IDK  WTF  I  AM  DOING", False, WHITE)
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)

        self.splash_text_left = self.font_text.render("©", False, DARK_GREY)        
        self.splash_rect_left = self.splash_text_left.get_rect(topleft=(self.title_rect.bottomleft[0] + 50, self.title_rect.midbottom[1]))

        self.splash_text_mid = self.font_text.render(" Tobi The Ghost ", False, DARK_GREY)        
        self.splash_rect_mid = self.splash_text_mid.get_rect(midtop=(self.title_rect.midbottom[0], self.title_rect.midbottom[1]))

        self.splash_text_right = self.font_text.render("1994", False, DARK_GREY)        
        self.splash_rect_right = self.splash_text_right.get_rect(topright=(self.title_rect.bottomright[0] - 50, self.title_rect.midbottom[1]))
    
    def get_event(self, event):
        if event.type == pygame.FINGERDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            self.color = DARK_BLUE
        if event.type == pygame.FINGERUP or event.type == pygame.MOUSEBUTTONUP:
            self.color = BLACK
            
    def update(self, dt):
        super().update(dt)
        self.time += dt
        if self.time >= self.end_time:
            self.next_state = "Main Menu"
            self.done = True

    def draw(self):
        self.splash_screen.fill(self.color)
        self.splash_screen.blits(((self.title, self.title_rect),
                    (self.splash_text_left, self.splash_rect_left),
                    (self.splash_text_mid, self.splash_rect_mid),
                    (self.splash_text_right, self.splash_rect_right)))
        
        pygame.display.get_surface().blit(self.splash_screen,(0,0))