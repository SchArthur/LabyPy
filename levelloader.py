from item import newItem
from alien import newAlien

class newLevel:
    def __init__(self,file : str):
        level_file = open(file,"r")
        
        self.load(level_file)

        level_file.close()

    def load(self, file):
        """
        Creer un dict des infos generales, 
        une liste des tuples des coords des monstres
        une liste des linges de cases de la carte
        """

        self.general = {}
        self.monsters = []
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
            elif '[map]' in file_lines[i]:
                lines_list = self.section_list(file_lines, i)
                for x in range(len(lines_list)):
                    self.map.append([])
                    values = lines_list[x].split(',')
                    for y in range(len(values)):
                        state = values[y]
                        if state.isnumeric():
                            self.map[x].append(int(values[y]))
                        else:
                            self.map[x].append(values[y])

    def section_list(self, lines_list, line_index):
        # Return la liste des lignes de la section
        List = []
        for i in range(line_index + 1, len(lines_list)):
            if '[' not in lines_list[i]:
                List.append(lines_list[i][:-1])
            else :
                break
        return List

level_file = newLevel('level_1.ini')
print(level_file.general)
print(level_file.monsters)
print(level_file.map)