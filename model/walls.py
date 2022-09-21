import pygame
class Walls():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
    
    def GetRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)