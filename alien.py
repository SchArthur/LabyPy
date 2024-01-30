import pygame
import random

class newAlien:
    def __init__(self, posX, posY,) -> None:
        self.position_x = posX
        self.position_y = posY
        self.next_move = 0-random.randrange(150,300)
        self.next_move = 0

    def draw(self, screen, tileSize, color_dict):
        item_color = color_dict["alien_color"]
        circle_center = (self.position_x*tileSize + tileSize/2, self.position_y*tileSize + tileSize/2)
        pygame.draw.circle(screen, item_color, circle_center, tileSize/2)

    def roam(self,deltaTime, labyrinthe, max_x, max_y):
        self.next_move += deltaTime
        if self.next_move > 0:
            old_pos = (self.position_x,self.position_y)
            direction = random.choice(('UP','DOWN','LEFT','RIGHT'))
            if direction == 'UP':
                self.position_y -= 1
                self.next_move = self.getRandomSpeed()
            elif direction == 'DOWN':
                self.position_y += 1
                self.next_move = self.getRandomSpeed()
            elif direction == 'LEFT':
                self.position_x -= 1
                self.next_move = self.getRandomSpeed()
            elif direction == 'RIGHT':
                self.position_x += 1
                self.next_move = self.getRandomSpeed()

            if self.position_y < 0:
                self.position_y = 0
                self.next_move = 1
            if self.position_y >= max_y:
                self.position_y = max_y-1
                self.next_move = 1
            if self.position_x < 0:
                self.position_x = 0
                self.next_move = 1
            if self.position_x > max_x:
                self.position_x = max_y-1
                self.next_move = 1
                
            if labyrinthe.getXY(self.position_x, self.position_y) == '1' :
                self.next_move = 1
                self.position_x = old_pos[0]
                self.position_y = old_pos[1]

    def getRandomSpeed(self):
        return random.randrange(-800,-300)
        

    def collect(self):
        self.isCollected = True
        print("Diamant récupéré !")
