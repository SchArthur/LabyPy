import pygame
import item

class Labyrinthe :
    # constructeur
    def __init__(self, sizeX, sizeY, from_list = False):
        """sizeX, sizeY désignent la taille du labyrinthe sur l'axe (x,y)"""
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.is_finished = False
        #attention création d'une matrice en Y X
        self.matrice = [ [0]* self.sizeX for _ in range(self.sizeY)]
        if from_list != False:
            self.set_from_list(from_list)

    def get_matrice(self):
        """renvoie la matrice associée au labyrinthe"""
        return self.matrice
    
    def getXY(self, i,j):
        """Renvoie la case (i,j) du labyrinthe sur l'axe (x,y)"""
        return self.matrice[j][i]

    def setXY(self, j,i,v):
        """Modifie par v la case (i,j) sur l'axe (x,y)"""
        self.matrice[j][i] = v
    
    def getSize(self):
        """Renvoie la taille (x,y) du labyrinthe"""
        return (self.sizeX, self.sizeY)
    
    def détruire_mur(self, i,j):
        """Détruit un mur du labyrinthe en (i,j) sur l'axe (x,y)"""
        self.matrice[j][i]=0

    def set_from_list(self, cell_list):
        for x in range(len(cell_list)):
            cell_line = cell_list[x]
            for y in range(len(cell_line)):
                self.setXY(x,y,cell_list[x][y])


    def set_from_file(self, fichier:str):
        """Lis et créer la matrice présente dans le fichier à l'adresse indiqué"""
        file = open(fichier, "r")
        list_lignes = file.readlines()
        for i in range(len(list_lignes)):
            liste_cases = list_lignes[i][:-1]
            liste_cases = liste_cases.split(',')
            for j in range(len(liste_cases)):
                self.setXY(j,i,liste_cases[j])
        file.close()

    def draw(self, screen, tilesize, color_dict):
        wall_color = color_dict['wall_color']
        finish_color = color_dict['finish_color']
        for i in range(len(self.matrice)):
            ligne = self.matrice[i]
            for j in range(len(ligne)):
                if self.matrice[i][j] == '1':
                    pygame.draw.rect(screen, wall_color, pygame.Rect(j*tilesize, i*tilesize, tilesize, tilesize))
                elif self.matrice[i][j] == 'A':
                    pygame.draw.line(screen, finish_color,(j*tilesize, i*tilesize),(j*tilesize + tilesize, i*tilesize + tilesize), 3)
                    pygame.draw.line(screen, finish_color,(j*tilesize + tilesize, i*tilesize),(j*tilesize, i*tilesize + tilesize), 3)

    def getPlayerPos(self):
        for i in range(len(self.matrice)):
            ligne = self.matrice[i]
            for j in range(len(ligne)):
                if self.matrice[i][j] == 'D':
                    return pygame.Vector2(j,i)

                
    def finish(self, item_list):
        items_collected = 0
        if not self.is_finished :
            for item in item_list:
                if item.isCollected :
                    items_collected +=1
            if items_collected == len(item_list):
                print('Arrivé avec tous les items, level validé')
                self.is_finished = True
            else:
                print('Il manque ' + str(len(item_list) - items_collected) + " diamant(s). Level en attente de validation, recherchez les objets manquants.")


