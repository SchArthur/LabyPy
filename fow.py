import pygame
import labyrinthe

view_range = 2

class fog_of_war:
    def __init__(self, sizeX, sizeY) -> None:
        self.sizeX = sizeX
        self.sizeY = sizeY

        self.matrice = [ [1]* self.sizeX for _ in range(self.sizeY) ]
    
    def draw(self, screen, tilesize,player_pos,labyrinthe:labyrinthe.Labyrinthe, color_dict):
        
        self.update(player_pos)
        for i in range(len(self.matrice)):
            ligne = self.matrice[i]
            for j in range(len(ligne)):
                if self.matrice[i][j] == 1:
                    pygame.draw.rect(screen, color_dict["fow_color_not_seen"], pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))
                elif self.matrice[i][j] == 2:
                    if labyrinthe.getXY(j,i) == 0:
                        pygame.draw.rect(screen, color_dict["fow_color_seen"], pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))
                    elif labyrinthe.getXY(j,i) == 1:
                        pygame.draw.rect(screen, color_dict["fow_color_wall_fog"], pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))

    def update(self, player_pos):
        """Mets à jouer le brouillard de guerre"""
        #les cases qui étaient à 0 sont mises sur 2
        for i in range(len(self.matrice)):
            ligne = self.matrice[i]
            for j in range(len(ligne)):
                if self.matrice[i][j] == 0:
                    self.matrice[i][j] = 2
        # les cases autour du joueur = 0
        for i in range(int(player_pos.x) - view_range, int(player_pos.x)+view_range +1):
            for j in range(int(player_pos.y) - view_range, int(player_pos.y)+view_range +1):
                if (i < self.sizeX) and (i >= 0) and (j < self.sizeY) and (j >= 0):
                    self.matrice[j][i] = 0
