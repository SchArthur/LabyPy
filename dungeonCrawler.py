# Example file showing a circle moving on screen
import pygame
import fow
import labyrinthe
import controller
from grid import Grid
import loaders
import entities
# pygame setup
pygame.init()

class newGame:
    def __init__(self) -> None:
        # LOADING
        self.level = loaders.loadLevel("level_1.ini")
        self.settings = loaders.loadConfig('config.ini')

        # SETTING
        self.player_speed = self.settings.player['player_speed']
        self.couleurs = self.settings.color
        self.tilesize = self.settings.general["tilesize"] # taille d'une tuile IG
        self.size = (self.level.general["size_x"], self.level.general["size_y"]) # taille du monde
        self.laby = labyrinthe.Labyrinthe(self.size[0],self.size[1], from_list=self.level.map)

        self.fps = 30 # fps du jeu
        self.next_move = 0 #tic avant déplacement

        self.clock = pygame.time.Clock()

        self.dt = 0
        self.show_grid = True
        self.show_pos = False

        self.screen = pygame.display.set_mode((self.size[0]*self.tilesize, self.size[1]*self.tilesize))
        # Labyrinthe


        self.brouillard = fow.fog_of_war(self.size[0],self.size[1])

        self.grid = Grid(self.size[0], self.size[1],self.tilesize)

        player_pos = self.laby.getPlayerPos()

        self.gridPressed = 0
        self.posPressed = 0

        # elements
        self.player = entities.Entity(player_pos, self.couleurs["player_color"], speed=self.player_speed)
        player_controller = controller.PlayerController(self.player, self)
        self.player.addController(player_controller)
        self.entities_list = []
        self.entities_list.append(self.player)
        self.item_list = self.level.create_diamonds()
        self.alien_list = self.level.create_aliens(self.couleurs["alien_color"])
        for elt in self.alien_list:
            alien_controller = controller.monsterController(elt,self)
            elt.addController(alien_controller)

        self.run()

    def run(self):
        self.running = True
        #tour de boucle, pour chaque FPS
        while self.running:
            self.screen.fill(self.couleurs["ground_color"])

            self.player.controller.Update()

            # affichage des différents composants
            # affichage de la grid
            if self.show_grid:
                self.grid.draw(self.screen, self.couleurs["grid_color"])

            # affichage du labyrinthe
            self.laby.draw(self.screen,self.tilesize,self.couleurs)
            for elt in self.item_list:
                elt.draw(self.screen,self.tilesize,self.couleurs)
            for elt in self.alien_list:
                elt.update()
                elt.draw(self.screen,self.tilesize)
            # self.brouillard.draw(self.screen,self.tilesize,self.player.pos,self.laby, self.couleurs)
            for elt in self.entities_list:
                elt.draw(self.screen, self.tilesize)
            
            pygame.display.flip()
            self.dt = self.clock.tick(self.fps)
        pygame.quit()

game = newGame()