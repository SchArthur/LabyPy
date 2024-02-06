import pygame

class Entity:
    def __init__(self, pos : pygame.Vector2, color : str, speed = 50, initiative=1, attaque=1, parade=1, nombre_attaque=1, nombre_parade=1, armure=1) -> None:
        self.color = color
        self.pos = pos
        self.speed = speed
        self.initiative = initiative
        self.attaque = attaque
        self.parade = parade
        self.nombre_attaque = nombre_attaque
        self.nombre_parade = nombre_parade
        self.armure = armure

    def addController(self, controller):
        self.controller = controller

    def draw(self, screen, tilesize):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos.x*tilesize, self.pos.y*tilesize, tilesize, tilesize))

    def update(self):
        if self.controller != None:
            self.controller.Update()

class newAlien(Entity):
    def draw(self, screen, tileSize):
        circle_center = (self.pos.x*tileSize + tileSize/2, self.pos.y*tileSize + tileSize/2)
        pygame.draw.circle(screen, self.color, circle_center, tileSize/2)