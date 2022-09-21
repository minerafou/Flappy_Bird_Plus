import pygame

pygame.init()

from model.player import Player
from model.walls import Walls

class Game():
    def __init__(self, screen, screen_height, screen_width):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.running = True

        self.game_screen = "play_scene"

        self.main_clock = pygame.time.Clock()

        self.player = Player(300, 200, 30, 30, (156, 44, 119))

        self.walls = []
        self.walls.append(Walls(0, 0, 50, 600, (225, 77, 42)))
        self.walls.append(Walls(750, 0, 50, 600, (225, 77, 42)))

        self.limit = screen_height
        self.have_to_quit = False
    
    def Run(self):
        while self.running:
            self.HandleEvent()
            self.Update()
            self.Refresh()
            self.main_clock.tick(60)
    
    def HandleEvent(self):

        self.mouse_pressed = False

        if self.have_to_quit:
            self.running = False

        #verifie les evenement pygame
        for event in pygame.event.get():
            #check des input joueur
            #input de la croix rouge (en haut a droite de la fenetre)
            if event.type == pygame.QUIT:
                self.running = False

            #check le temps
            if event.type == pygame.USEREVENT:
                self.EveryTenMilliSecAction()
            
            #check input clavier
            if self.game_screen == "play_scene":
                #check for 1 input key
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #left button
                        self.mouse_pressed = True

                    elif event.button == 3:
                        #right button
                        pass
                    
                    elif event.button == 2:
                        #middle button
                        pass

    def Update(self):
        #update screen size
        self.screen_width, self.screen_height = self.screen.get_size()

        #delete tous sur l'ecran
        self.screen.fill((253, 132, 31))

        if self.game_screen == "play_scene":
            self.have_to_quit = self.player.Update(self.mouse_pressed, self.walls, self.limit)

            self.player.Draw(self.screen)

            for i in self.walls:
                i.Draw(self.screen)
    
    def Refresh(self):
        pygame.display.flip()

    def EveryTenMilliSecAction(self):
        pass

pygame.time.set_timer(pygame.USEREVENT, 10)

screen_width = 800
screen_height = 600

#set la fenetre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird Plus")

#cree le jeu a partir le l'objet 'game'
game1 = Game(screen, screen_width, screen_height)

#lance la boucle global
game1.Run()

#quitte pygame
pygame.quit()