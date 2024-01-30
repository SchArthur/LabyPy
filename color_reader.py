class color_read():
    def readFile(self,file:str) -> dict :
        color_file = open(file,"r")
        premiere_ligne = color_file.readline().split(",")
        file_format = premiere_ligne[0]
        if file_format != 'ini':
            raise ValueError("Wrong file format")
        else :
            self.color_dict = {}
            self.color_dict["VERSION"] = premiere_ligne[1]
            self.color_dict["AUTEUR"] = premiere_ligne[2][:-1]

            for ligne in color_file.readlines():
                split_ligne = ligne.split('=')
                self.color_dict[split_ligne[0]] = split_ligne[1][:-1]

        color_file.close()
        return self.color_dict

test = color_read()
print(test.readFile("color.ini")["ground_color"])

