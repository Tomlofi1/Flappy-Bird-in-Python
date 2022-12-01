import pygame
from game import Game
from menu import Menu



class Main:
    def __init__(self):
        
        self.loop = True
        self.window = pygame.display.set_mode([360, 640])
        self.title = pygame.display.set_caption('Flappy Bird')
        self.fps = pygame.time.Clock()
        self.game = Game()
        self.menu = Menu()
        

        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(event)
    
    def draw(self):
        
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update(str(self.game.max_score))
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.updates()
        else:
            self.loop = False


    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw() 
            pygame.display.update()
            pygame.font.init()
            pygame.mixer.init()

loop = True
while loop:
    Main().update()
