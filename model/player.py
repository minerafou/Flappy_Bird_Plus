import pygame
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.dir = "left"

        self.velocity_x = 5
        self.velocity_y = 0
    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
    
    def Update(self, mouse_pressed, walls, limit):
        if mouse_pressed:
            self.velocity_y = -5
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_y += 0.3

        for i in walls:
            if i.GetRect().colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
                if self.dir == "left":
                    self.dir = "right"
                    self.velocity_x = -5
                else:
                    self.dir = "left"
                    self.velocity_x = 5
        
        if self.y + self.height > limit:
            return True
        return False
