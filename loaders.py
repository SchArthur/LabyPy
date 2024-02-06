from item import newItem
from entities import newAlien
from controller import monsterController
import pygame

class Loader:
    def __init__(self, file : str):
        File = open(file,"r")
        
        self.load(File)

        File.close()

    def section_list(self, lines_list, line_index):
        # Return la liste des lignes de la section
        List = []
        for i in range(line_index + 1, len(lines_list)):
            if '[' not in lines_list[i]:
                List.append(lines_list[i][:-1])
            else :
                break
        return List
    
class loadConfig(Loader):
    def load(self, file):
        """
        Creer un dict des infos generales, 
        un dict des couleurs
        un dict des infos du joueur
        """

        self.general = {}
        self.color = {}
        self.player = {}

        file_lines = file.readlines()

        for i in range(len(file_lines)):
            if '[general]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for line in lines_list:
                    values = line.split('=')
                    if values[1].isnumeric():
                        values[1] = int(values[1])
                    self.general[values[0]] = values[1]
            elif '[color]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for line in lines_list:
                    values = line.split('=')
                    self.color[values[0]] = values[1]
            elif '[player]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for line in lines_list:
                    values = line.split('=')
                    if values[1].isnumeric():
                        values[1] = int(values[1])
                    self.player[values[0]] = values[1]
        
class loadLevel(Loader):

    def load(self, file):
        """
        Creer un dict des infos generales, 
        une liste des tuples des coords des monstres
        une liste des linges de cases de la carte
        """

        self.general = {}
        self.monsters = []
        self.diamonds = []
        self.map = []

        file_lines = file.readlines()

        for i in range(len(file_lines)):
            if '[general]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for line in lines_list:
                    values = line.split('=')
                    if values[1].isnumeric():
                        values[1] = int(values[1])
                    self.general[values[0]] = values[1]
            elif '[monsters]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for line in lines_list:
                    values = line.split(',')
                    self.monsters.append((int(values[0]), int(values[1])))
            elif '[diamonds]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for line in lines_list:
                    values = line.split(',')
                    self.diamonds.append((int(values[0]), int(values[1])))
            elif '[map]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for x in range(len(lines_list)):
                    self.map.append([])
                    values = lines_list[x].split(',')
                    for y in range(len(values)):
                        self.map[x].append(values[y])

    def create_aliens(self, color):
        monsters = []
        for elt in self.monsters:
            pos = pygame.Vector2(elt[0], elt[1])
            monsters.append(newAlien(pos, color))
            
        return monsters
    
    def create_diamonds(self):
        diamonds = []
        for elt in self.diamonds:
            diamonds.append(newItem(elt[0],elt[1]))
        return diamonds