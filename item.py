import pygame

class newItem:
    def __init__(self, posX, posY) -> None:
        self.position_x = posX
        self.position_y = posY

    def draw(self, screen, tileSize, color_dict):
        item_color = color_dict["item_color"]
        triangle_points = ((self.position_x*tileSize, self.position_y*tileSize + tileSize),
                           (self.position_x*tileSize + tileSize, self.position_y*tileSize + tileSize),
                           (self.position_x*tileSize + tileSize/2, self.position_y*tileSize))
        pygame.draw.lines(screen, item_color, True,triangle_points, 5)