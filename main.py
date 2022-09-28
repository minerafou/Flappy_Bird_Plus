import pygame

pygame.init()

from model.player import Player
from model.level import Levels

class Game():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.running = True

        self.game_screen = "play_scene"

        self.main_clock = pygame.time.Clock()

        self.player = Player(300, 200, 30, 30, (156, 44, 119))

        self.limit = screen_height
        self.have_to_quit = False

        self.camera_y = 0

        self.upest_level_number = 1
        self.level_down = Levels(0)
        self.level_up = Levels(1)

        self.lava_height = screen_height
        #156, 44, 119
    
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
            self.have_to_quit, self.camera_y = self.player.Update(self.mouse_pressed, self.level_up.GetLevel(), self.level_down.GetLevel(), self.limit, self.camera_y, self.upest_level_number)

            #set level limit
            self.limit = self.screen_height - self.camera_y

            #change level
            if self.camera_y > (self.upest_level_number * self.screen_height):
                self.upest_level_number += 1
                self.level_down = self.level_up
                self.level_up = Levels(2)

            self.player.Draw(self.screen, self.camera_y)

            self.level_up.DrawLevel(self.screen, self.camera_y, self.upest_level_number)
            self.level_down.DrawLevel(self.screen, self.camera_y, self.upest_level_number - 1)

            #draw lava
            self.lava_rect = pygame.Rect(50, self.lava_height, 700, screen_height)
            self.lava_rect_draw = pygame.Rect(50, self.lava_height + self.camera_y, 700, screen_height)
            pygame.draw.rect(self.screen, (156, 44, 119), self.lava_rect_draw)
            #update for lava
            self.lava_height -= 1
            #collid lava
            if self.player.GetRect().colliderect(self.lava_rect):
                self.have_to_quit = True
    
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