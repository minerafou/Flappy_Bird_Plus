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
    def Draw(self, screen, camera_y):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y + camera_y, self.width, self.height))
    
    def Update(self, mouse_pressed, level_up, level_down, limit, camera_y, upest_level_number):
        if mouse_pressed:
            self.velocity_y = -5
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_y += 0.3

        collid = False
        for i in level_down:
            if i.GetRect(upest_level_number - 1).colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
                if self.dir == "left":
                    self.dir = "right"
                    self.velocity_x = -5
                else:
                    self.dir = "left"
                    self.velocity_x = 5
                collid = True

        for i in level_up:
            if collid:
                pass
            elif i.GetRect(upest_level_number).colliderect(pygame.Rect(self.x, self.y, self.width, self.height)):
                if self.dir == "left":
                    self.dir = "right"
                    self.velocity_x = -5
                else:
                    self.dir = "left"
                    self.velocity_x = 5
        
        if self.y < 100 - camera_y:
            camera_y = 100 - self.y
        
        if self.y + self.height > limit:
            return True, camera_y
        return False, camera_y

    def GetRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)