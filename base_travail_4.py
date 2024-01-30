# Example file showing a circle moving on screen
import pygame
import fow
import labyrinthe
from inputController import inputControl
from grid import Grid
# pygame setup
pygame.init()

#constantes
tilesize = 32 # taille d'une tuile IG
size = (20, 10) # taille du monde
fps = 30 # fps du jeu
player_speed = 150 # vitesse du joueur
next_move = 0 #tic avant déplacement

# color
ground_color = "#EDDACF"
grid_color = "#7F513D"
player_color = "#9F715D"


screen = pygame.display.set_mode((size[0]*tilesize, size[1]*tilesize))
clock = pygame.time.Clock()
running = True
dt = 0
show_grid = True
show_pos = False

player_pos = pygame.Vector2(size[0]//8, size[1]//2)

# Labyrinthe
laby = labyrinthe.Labyrinthe(size[0],size[1])
laby.set_from_file("laby-01.csv")
brouillard = fow.fog_of_war(size[0],size[1])

grid = Grid(size[0], size[1],tilesize)

input = inputControl()
gridPressed = 0
posPressed = 0

#tour de boucle, pour chaque FPS
while running:
    screen.fill(ground_color)

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
        if player_pos.y < 0:
            player_pos.y = 0
        if player_pos.y >= size[1]:
            player_pos.y = size[1]-1
        if player_pos.x < 0:
            player_pos.x = 0
        if player_pos.x > size[0]-1:
            player_pos.x = size[0]-1

        if laby.getXY(int(player_pos.x),int(player_pos.y)) == 1 :
            player_pos = old_pos.copy()

    if show_pos:
        print("pos: ",player_pos)


    # affichage des différents composants
    # affichage de la grid
    if show_grid:
        grid.draw(screen, grid_color)

    # affichage du labyrinthe
    laby.draw(screen,tilesize)
    brouillard.draw(screen,tilesize,player_pos,laby)

    #affichage du joueur
    pygame.draw.rect(screen, player_color, pygame.Rect(player_pos.x*tilesize, player_pos.y*tilesize, tilesize, tilesize))

    pygame.display.flip()
    dt = clock.tick(fps)

pygame.quit()