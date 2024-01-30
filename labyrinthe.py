import pygame

class Labyrinthe :
    # constructeur
    def __init__(self, sizeX, sizeY):
        """sizeX, sizeY désignent la taille du labyrinthe sur l'axe (x,y)"""
        self.sizeX = sizeX
        self.sizeY = sizeY
        #attention création d'une matrice en Y X
        self.matrice = [ [0]* self.sizeX for _ in range(self.sizeY) ]

    def affiche(self):
        """Sortie console du labyrinthe"""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                # rappel: matrice en Y,X
                print(self.matrice[j][i], end = "")
            print()
        #print(self.matrice)

    def get_matrice(self):
        """renvoie la matrice associée au labyrinthe"""
        return self.matrice
    
    def getXY(self, i,j):
        """Renvoie la case (i,j) du labyrinthe sur l'axe (x,y)"""
        return self.matrice[j][i]

    def setXY(self, i,j,v):
        """Modifie par v la case (i,j) sur l'axe (x,y)"""
        self.matrice[j][i] = v
    
    def getSize(self):
        """Renvoie la taille (x,y) du labyrinthe"""
        return (self.sizeX, self.sizeY)
    
    def détruire_mur(self, i,j):
        """Détruit un mur du labyrinthe en (i,j) sur l'axe (x,y)"""
        self.matrice[j][i]=0

    def set_from_file(self, fichier:str):
        """Lis et créer la matrice présente dans le fichier à l'adresse indiqué"""
        file = open(fichier, "r")
        list_lignes = file.readlines()
        for i in range(len(list_lignes)):
            liste_cases = list_lignes[i][:-1]
            print(liste_cases)
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


"""
laby = Labyrinthe(20,10)

laby.set_from_file("laby-01.csv")

print(laby.matrice[2][4])
"""