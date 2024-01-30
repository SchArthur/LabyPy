import pygame



class inputControl:
    nextMove= 0
    
    def __init__(self) -> None:
        self.keys= { "UP":0 , "DOWN":0, "LEFT":0, "RIGHT":0, "QUIT":0, "GRID": 0, "POS":0}

    def keyPressed(self):
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

        return self.keys
    