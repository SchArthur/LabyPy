import pygame

class Grid:
    def __init__(self, X, Y, tileSize) -> None:
        self.tileSize = tileSize
        self.sizeX = X
        self.sizeY = Y

    def draw(self, screen, grid_color):
        for i in range(1,self.sizeX):
            pygame.draw.line(screen,grid_color, (self.tileSize*i, 0), (self.tileSize*i, self.tileSize*self.sizeX))
        for i in range(0,self.sizeY):
            pygame.draw.line(screen,grid_color, (0, self.tileSize*i), (self.tileSize*self.sizeX, self.tileSize*i))