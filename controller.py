import pygame
import entities
import random
import combat

class MovementController :
    nextMove = 0
    def __init__(self, entity : entities.Entity, game) -> None:
        self.entity = entity
        self.game = game
        self.canUp = False
        self.canDown = False
        self.canRight = False
        self.canLeft = False
        self.next_move = 0
        self.keys= { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0}

    def Update(self):
        self.next_move += self.game.dt
        # gestion des déplacements
        if self.next_move>0:
            self.checkMovement()
            self.canMoveAround()
            if self.keys['UP'] == 1 and self.canUp:
                self.entity.pos.y -= 1
                self.next_move = -self.entity.speed
            elif self.keys['DOWN'] == 1 and self.canDown:
                self.entity.pos.y += 1
                self.next_move = -self.entity.speed
            elif self.keys['LEFT'] == 1 and self.canLeft :
                self.entity.pos.x -= 1
                self.next_move = -self.entity.speed
            elif self.keys['RIGHT'] == 1 and self.canRight:
                self.entity.pos.x += 1
                self.next_move = -self.entity.speed

        collision_list = self.checkCollisions(self.entity.pos)
        if ('ENTITIES' in collision_list) and (collision_list['ENTITIES'] != []) and (self.entity.type == 'PLAYER'):
            for elt in collision_list['ENTITIES']:
                print(self, 'collided with :', elt)
                combat.combat(self.entity, elt)

        if self.next_move == -self.entity.speed:
            if self.game.laby.getXY(int(self.entity.pos.x),int(self.entity.pos.y)) == 'A' :
                self.game.laby.finish(self.game.item_list, self.game)

    def canMoveAround(self):
        up_tile = (int(self.entity.pos.x),int(self.entity.pos.y-1))
        self.canUp = self.checkMoveAt(up_tile)

        down_tile = (int(self.entity.pos.x),int(self.entity.pos.y+1))
        self.canDown = self.checkMoveAt(down_tile)

        left_tile = (int(self.entity.pos.x-1),int(self.entity.pos.y))
        self.canLeft = self.checkMoveAt(left_tile)

        right_tile = (int(self.entity.pos.x+1),int(self.entity.pos.y))
        self.canRight = self.checkMoveAt(right_tile)

    def checkMoveAt(self, tileToCheck) -> bool :
        x = tileToCheck[0]
        y = tileToCheck[1]
        if (y < 0) or (y >= self.game.size[1]) or (x < 0) or (x >= self.game.size[0]):
            return False
        else :
            if self.game.laby.getXY(x, y) == '1' :
                return False
            else :
                return True
    
class monsterController(MovementController):
    def checkMovement(self):
        self.entity.speed = random.randrange(150,400)
        random_dir = random.randrange(4)
        if random_dir == 0:
            self.keys['UP'] = 1
            self.keys['DOWN'] = 0
            self.keys['LEFT'] = 0
            self.keys['RIGHT'] = 0
        elif random_dir == 1:
            self.keys['UP'] = 0
            self.keys['DOWN'] = 1
            self.keys['LEFT'] = 0
            self.keys['RIGHT'] = 0
        elif random_dir == 2:
            self.keys['UP'] = 0
            self.keys['DOWN'] = 0
            self.keys['LEFT'] = 1
            self.keys['RIGHT'] = 0
        elif random_dir == 3:
            self.keys['UP'] = 0
            self.keys['DOWN'] = 0
            self.keys['LEFT'] = 0
            self.keys['RIGHT'] = 1

    def checkCollisions(self, pos):
        entities_collided = []
        items_collided = []
        player_collided = []
        for elt in self.game.alien_list:
            if elt.controller != self:
                if (self.entity.pos.x, self.entity.pos.y) == (elt.pos.x, elt.pos.y):
                    entities_collided.append(elt)
                    self.pos = pos
        if (self.entity.pos.x, self.entity.pos.y) == (self.game.player.pos.x, self.game.player.pos.y):
            player_collided.append(self.game.player)
        dict = {'ENTITIES': entities_collided, 'PLAYER' : player_collided, 'ITEMS': items_collided}
        return dict


class PlayerController(MovementController):
    def __init__(self, entity, game):
        super().__init__(entity, game)
        self.special_keys= {"QUIT":0, "GRID": 0, "POS":0, "MOUSE_COORDS": [0,0]}
        self.gridPressed = False
        self.posPressed = False
        self.keys.update(self.special_keys)

    def checkCollisions(self, pos):
        entities_collided = []
        items_collided = []
        for elt in self.game.alien_list:
            if elt.controller != self:
                if (self.entity.pos.x, self.entity.pos.y) == (elt.pos.x, elt.pos.y):
                    entities_collided.append(elt)
        for elt in self.game.item_list:
            if (self.entity.pos.x, self.entity.pos.y) == (elt.pos.x, elt.pos.y):
                if not elt.isCollected:
                    elt.collect()
                items_collided.append(elt)
        dict = {'ENTITIES': entities_collided, 'ITEMS': items_collided}
        return dict

    def checkMovement(self):
        keys = self.checkInputs()

    def checkInputs(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    self.keys['UP'] = 1
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.keys['DOWN'] = 1
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    self.keys['LEFT'] = 1
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.keys['RIGHT'] = 1

                if event.key == pygame.K_ESCAPE:
                    self.keys['QUIT'] = 1
                if event.key == pygame.K_g:
                    self.keys['GRID'] = 1
                if event.key == pygame.K_p:
                    self.keys['POS'] = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z or event.key == pygame.K_UP:
                    self.keys['UP'] = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.keys['DOWN'] = 0
                if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                    self.keys['LEFT'] = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.keys['RIGHT'] = 0

                if event.key == pygame.K_ESCAPE:
                    self.keys['QUIT'] = 0
                if event.key == pygame.K_g:
                    self.keys['GRID'] = 0
                if event.key == pygame.K_p:
                    self.keys['POS'] = 0

            if event.type == pygame.QUIT:
                self.keys['QUIT'] = 1
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print("mouse_pos:", pos)
                self.keys['MOUSE_COORDS'] = pos
        self.checkSpecialInputs()
        return self.keys
    
    def checkSpecialInputs(self):
        # Quit game
            if self.keys["QUIT"] == 1:
                self.game.running = False

            # Show grid
            if self.keys["GRID"] == 1 and not self.gridPressed:
                self.game.show_grid = not self.game.show_grid
                self.gridPressed = True
            if self.keys["GRID"] == 0 and self.gridPressed:
                self.gridPressed = False

            if self.keys["POS"] == 1 and not self.posPressed:
                self.game.show_pos = not self.game.show_pos
                self.posPressed = True
            if self.keys["POS"] == 0 and self.posPressed:
                self.posPressed = False