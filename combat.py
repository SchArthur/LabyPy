import entities
import random

def combat(player : entities.newPlayer, enemy : entities):
    print("Combat de", player, "contre", enemy)
    starter = diceFight(player.attaque, tries=2, default= 1)
    Results = 2
    if starter == 1:
        print('le joueur commence')
        attaquant = player
        victime = enemy
    else :
        print('alien commence')
        attaquant = enemy
        victime = attaquant
    while Results == 2 :
        attaque(attaquant, victime)
        Results = testResults(attaquant, victime)
        attaquant, victime = victime, attaquant
        print(attaquant, victime)

    print(player.getStats())
    print(enemy.getStats())
    raise ValueError("fight over")

def testResults(attaquant, victime):
    if (victime.nombre_attaque <= 0) and (attaquant.nombre_attaque <= 0):
        print("plus personne ne peut attaquer")
        return 0
    if (victime.pv <= 0):
        print(attaquant, 'a gagné')
        return 1
    else :
        print('next round')
        return 2

def attaque(attaquant : entities, victime : entities):
    # renvoie true si le combat est fini
    if attaquant.nombre_attaque > 0:
        premier_lancer = diceFight(attaquant.attaque, victime.parade, default=2)
        if premier_lancer == 1:
            print("Attaque réussi pour l'attaquant")
            attaquant.nombre_attaque -= 1
            lancer_attaque = diceThrow()
            if victime.nombre_parade > 0:
                if lancer_attaque > victime.armure :
                    print("L'attaque perce l'armure ! -1 pv pour :", victime)
                    victime.pv -= 1
                else :
                    print("L'armure de", victime ,"bloque l'attaque !")
                    victime.nombre_parade -=1
            else:
                print(victime, "ne peut plus se défendre ! -1 pv")
        else :
            print('Attaque echoué pour', attaquant)
            attaquant.nombre_attaque -= 1
    else:
        print(attaquant, "ne peut plus attaquer !")

def diceFight(stat_1 = 0, stat_2 = 0, tries = 1, faces = 6, default = 0):
    for i in range(0, tries):
        lancer_1 = diceThrow(faces) + stat_1
        lancer_2 = diceThrow(faces) + stat_2
        print("Lancé 1 :", lancer_1,". Lancé 2 :", lancer_2,".")
        print(lancer_1, lancer_2)
        if lancer_1 > lancer_2 :
            return 1
        elif lancer_2 > lancer_1 :
            return 2
    return default

def diceThrow(faces = 6):
    # renvoi le résulat d'un lancé de dé à 'faces' faces
    return random.randrange(0, faces+1)