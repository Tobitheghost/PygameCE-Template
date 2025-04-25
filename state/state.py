import pygame

class State:
    def __init__(self, game, name) -> None:
        self.game = game
        self.name = name
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = self.game.screen.get_rect()
        self.persist = {}
        self.font_title = pygame.font.Font(None, 48)
        self.font_text = pygame.font.Font(None, 24)
    
    def startup(self, persistent):
        self.persist = persistent
        
    def get_event(self, event:pygame.Event):
        if event.type == pygame.QUIT:
            self.quit == True
    
    def update(self, dt):
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.next_state = "Main Menu"
            self.done = True
    
    def draw(self):
        ...
