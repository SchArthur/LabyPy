# Example file showing a circle moving on screen
import pygame
import fow
import labyrinthe
from inputController import inputControl
from grid import Grid
from color_reader import color_read
import item
import levelloader
# pygame setup
pygame.init()

#constantes


fps = 30 # fps du jeu
player_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement

# color
couleurs = color_read().readFile("color.ini")


clock = pygame.time.Clock()
running = True
dt = 0
show_grid = True
show_pos = False

#LEVEL
level_file = "level-02.csv"
level = levelloader.newLevel(level_file)
tilesize = level.level_dict["TILESIZE"] # taille d'une tuile IG
size = (level.level_dict["SIZE_X"], level.level_dict["SIZE_Y"]) # taille du monde

screen = pygame.display.set_mode((size[0]*tilesize, size[1]*tilesize))
# Labyrinthe
laby = labyrinthe.Labyrinthe(size[0],size[1])
laby.set_from_file(level.level_dict["LABY_FILE"])
brouillard = fow.fog_of_war(size[0],size[1])

grid = Grid(size[0], size[1],tilesize)

player_pos = laby.getPlayerPos()

input = inputControl()
gridPressed = 0
posPressed = 0

item_list = level.item_list
alien_list = level.alien_list

#tour de boucle, pour chaque FPS
while running:
    screen.fill(couleurs["ground_color"])

    # lecture clavier / souris

    keysPressed = input.keyPressed()

    # Quit game
    if keysPressed["QUIT"] == 1:
        running = False

    # Show grid
    if keysPressed["GRID"] == 1 and not gridPressed:
        show_grid = not show_grid
        gridPressed = True
    if keysPressed["GRID"] == 0 and gridPressed:
        gridPressed = False


    if keysPressed["POS"] == 1 and not posPressed:
        show_pos = not show_pos
        posPressed = True
    if keysPressed["POS"] == 0 and posPressed:
        posPressed = False


    next_move += dt
    # gestion des déplacements
    if next_move>0:
        old_pos = player_pos.copy()
        if keysPressed['UP'] == 1:
            player_pos.y -= 1
            next_move = -player_speed
        elif keysPressed['DOWN'] == 1:
            player_pos.y += 1
            next_move = -player_speed
        elif keysPressed['LEFT'] == 1:
            player_pos.x -= 1
            next_move = -player_speed
        elif keysPressed['RIGHT'] == 1:
            player_pos.x += 1
            next_move = -player_speed

        # vérification du déplacement du joueur pour ne pas sortir de la fenetre
        if next_move == -player_speed:
            if player_pos.y < 0:
                player_pos.y = 0
                next_move = 0
            if player_pos.y >= size[1]:
                player_pos.y = size[1]-1
                next_move = 0
            if player_pos.x < 0:
                player_pos.x = 0
                next_move = 0
            if player_pos.x > size[0]-1:
                player_pos.x = size[0]-1
                next_move = 0

            #detection de collisions
            if laby.getXY(int(player_pos.x),int(player_pos.y)) == '1' :
                player_pos = old_pos.copy()
            if laby.getXY(int(player_pos.x),int(player_pos.y)) == 'A' :
                laby.finish(item_list)
            for elt in item_list:
                if (player_pos.x, player_pos.y) == (elt.position_x, elt.position_y):
                    if not elt.isCollected:
                        elt.collect()
        for elt in alien_list:
            if (player_pos.x, player_pos.y) == (elt.position_x, elt.position_y):
                player_pos = laby.getPlayerPos()

    if show_pos:
        print("pos: ",player_pos)


    # affichage des différents composants
    # affichage de la grid
    if show_grid:
        grid.draw(screen, couleurs["grid_color"])

    # affichage du labyrinthe
    laby.draw(screen,tilesize,couleurs)
    for elt in item_list:
        elt.draw(screen,tilesize,couleurs)
    for elt in alien_list:
        elt.roam(dt, laby, size[0], size[1])
        elt.draw(screen,tilesize,couleurs)
    brouillard.draw(screen,tilesize,player_pos,laby, couleurs)



    #affichage du joueur
    pygame.draw.rect(screen, couleurs["player_color"], pygame.Rect(player_pos.x*tilesize, player_pos.y*tilesize, tilesize, tilesize))

    pygame.display.flip()
    dt = clock.tick(fps)

pygame.quit()