import pygame, time
from game.settings import *
from screens.clicker.clicker import Clicker
from screens.splash.splash import SplashScreen
from screens.main_menu.main_menu import Main_Menu
from screens.parallax.parallax import Parallax

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH * SCREEN_SCALE, SCREEN_HEIGHT * SCREEN_SCALE])
        self.delta_time, self.previous_time = 0, time.time()
        self.fps = 0
        self.sec_timer = 0
        self.frame_counter = 0
        self.running = True
        self.states = {"Splash":SplashScreen, "Clicker":Clicker, "Main Menu":Main_Menu, "Parallax":Parallax}
        self.state = Main_Menu(self)
        
    def set_state(self, state:str):
        self.state = self.states[state](self)
        self.state.done = False
    
    def quit_game(self, event:pygame.Event):
        if event.type == pygame.QUIT:
            self.running = False
    
    def get_event(self):
        for event in pygame.event.get():
            self.quit_game(event)
            self.state.get_event(event)
    
    def get_delta(self):
        self.delta_time = time.time() - self.previous_time
        self.previous_time = time.time()
        self.sec_timer += self.delta_time
        self.frame_counter += 1
        if self.sec_timer >= 1:
            self.sec_timer = 0
            self.fps = self.frame_counter
            self.frame_counter = 0
    
    def update(self):
        self.get_delta()
        self.get_event()
        self.state.update(self.delta_time)
        
        if self.state.done:
            self.set_state(self.state.next_state)
            
        pygame.display.set_caption(str(self.fps))
    
    def draw(self):
        self.state.draw()
        pygame.display.update()
    
    def run(self):
        while self.running:
            self.update()
            self.draw()