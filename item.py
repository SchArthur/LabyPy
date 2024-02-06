import pygame

class newItem:
    def __init__(self, posX, posY) -> None:
        self.isCollected = False
        self.pos = pygame.Vector2(posX,posY)

    def draw(self, screen, tileSize, color_dict):
        if not self.isCollected :
            item_color = color_dict["item_color"]
            triangle_points = ((self.pos.x*tileSize, self.pos.y*tileSize + tileSize),
                            (self.pos.x*tileSize + tileSize, self.pos.y*tileSize + tileSize),
                            (self.pos.x*tileSize + tileSize/2, self.pos.y*tileSize))
            pygame.draw.lines(screen, item_color, True,triangle_points, 5)

    def collect(self):
        self.isCollected = True
        print("Diamant récupéré !")
