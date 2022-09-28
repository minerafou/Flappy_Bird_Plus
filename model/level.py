from model.walls import Walls
class Levels():
    def __init__(self, index):
        self.index = index
        self.walls = []
        self.walls.append(Walls(0, 0, 50, 600, (225, 77, 42)))
        self.walls.append(Walls(750, 0, 50, 600, (225, 77, 42)))
        self.walls.append(Walls(50, 0, 50, 50, (225, 77, 42)))
    
    def DrawLevel(self, screen, camera_y, upest_level_number):
        for i in self.walls:
            i.Draw(screen, camera_y, upest_level_number)
    
    def GetLevel(self):
        return self.walls
