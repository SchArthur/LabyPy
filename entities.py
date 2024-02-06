import pygame

class Entity:
    def __init__(self, pos : pygame.Vector2, color : str, speed = 50, initiative=1, attaque=1, parade=1, nombre_attaque=1, nombre_parade=1, armure=1, pv=3, enchainemnt = 100) -> None:
        self.color = color
        self.pos = pos
        self.speed = speed
        self.initiative = initiative
        self.attaque = attaque
        self.parade = parade
        self.nombre_attaque = nombre_attaque
        self.nombre_parade = nombre_parade
        self.armure = armure
        self.pv = pv
        self.enchainemnt = enchainemnt

    def getStats(self):
        stat_list = {'attaque_restantes' : self.nombre_attaque,
                     'parade_restantes' : self.nombre_parade,
                     'pv': self.pv}
        return stat_list

    def addController(self, controller):
        self.controller = controller

    def draw(self, screen, tilesize):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.pos.x*tilesize, self.pos.y*tilesize, tilesize, tilesize))

    def Update(self, deltaTime):
        if self.controller != None:
            self.controller.Update()

class newAlien(Entity):
    def __init__(self, pos: pygame.Vector2, color: str, speed=50, initiative=5, attaque=1, parade=1, nombre_attaque=1, nombre_parade=1, armure=1, pv=1, enchainemnt = 90) -> None:
        super().__init__(pos, color, speed, initiative, attaque, parade, nombre_attaque, nombre_parade, armure, pv, enchainemnt)
        self.type = 'ALIEN'

    def draw(self, screen, tileSize):
        circle_center = (self.pos.x*tileSize + tileSize/2, self.pos.y*tileSize + tileSize/2)
        pygame.draw.circle(screen, self.color, circle_center, tileSize/2)

class newPlayer(Entity):
    def __init__(self, pos: pygame.Vector2, color: str, speed=50, initiative=2, attaque=1, parade=2, nombre_attaque=1, nombre_parade=2, armure=2, pv=3, enchainemnt = 110) -> None:
        super().__init__(pos, color, speed, initiative, attaque, parade, nombre_attaque, nombre_parade, armure, pv ,enchainemnt)
        self.type = 'PLAYER'