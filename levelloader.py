from item import newItem
from alien import newAlien

class newLevel:
    def __init__(self,file):
        level_file = open(file,"r")
        self.item_list = []
        self.alien_list=[]

        # file format
        premiere_ligne = level_file.readline().split(",")
        file_format = premiere_ligne[0]
        if file_format != 'ini':
            raise ValueError("Wrong file format")
        else :
            self.level_dict = {}
            self.level_dict["VERSION"] = premiere_ligne[1]
            self.level_dict["AUTEUR"] = premiere_ligne[2][:-1]

        #size et tilesize
        next_ligne = level_file.readline().split(",")
        self.level_dict["TILESIZE"] = int(next_ligne[0])
        self.level_dict["SIZE_X"] = int(next_ligne[1])
        self.level_dict["SIZE_Y"] = int(next_ligne[2][:-1])
        
        # laby file
        next_ligne = level_file.readline().split(",")
        self.level_dict["LABY_FILE"] = next_ligne[0]
        
        #items
        next_ligne = level_file.readline().split(",")
        self.level_dict["ITEM_TOTAL"] = int(next_ligne[0])
        for i in range(0, int(self.level_dict["ITEM_TOTAL"])):
            next_ligne = level_file.readline().split(",")
            self.level_dict["ITEM_" + str(i + 1) + "_X"] = int(next_ligne[0])
            self.level_dict["ITEM_" + str(i + 1) + "_Y"] = int(next_ligne[1])
            self.item_list.append(newItem(int(next_ligne[0]),int(next_ligne[1])))

        next_ligne = level_file.readline().split(",")
        self.level_dict["ALIEN_TOTAL"] = int(next_ligne[0])
        for i in range(0, int(self.level_dict["ALIEN_TOTAL"])):
            next_ligne = level_file.readline().split(",")
            self.level_dict["ALIEN_" + str(i + 1) + "_X"] = int(next_ligne[0])
            self.level_dict["ALIEN_" + str(i + 1) + "_Y"] = int(next_ligne[1])
            self.alien_list.append(newAlien(int(next_ligne[0]),int(next_ligne[1])))

        level_file.close()