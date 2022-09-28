import pygame
class Walls():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def Draw(self, screen, camera_y, upest_level_number):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y + camera_y - (upest_level_number * 600), self.width, self.height))
    
    def GetRect(self, upest_level_number):
        return pygame.Rect(self.x, self.y - (upest_level_number * 600), self.width, self.height)