import pygame
from pygame.locals import*

class Niveau :

    # Constructeur
    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    #rempli self.structure à partir de level.txt
    def generer(self):
        with open(self.fichier, "r") as fichier:
            structure_niveau =[]

            for ligne in fichier :
                ligne_niveau = []

                for brique in ligne :
                    if brique != '\n':
                        ligne_niveau.append(brique)

                structure_niveau.append(ligne_niveau)
            
        self.structure = structure_niveau

    #affiche le nombre de ligne de brique demandé
    def affiche_ligne(self, fenetre,num_ligne):
        brique = pygame.image.load("mur.png")
        
        num_ligne= num_ligne - 1
        
        cpt_ligne = num_ligne
        cpt_ligne_inverse = 0
        while (cpt_ligne >=0) :
            y = 15 + 30*cpt_ligne
            
            cpt_sprite = 0
            for sprite in self.structure[cpt_ligne_inverse] :
                x = 15 + 30*cpt_sprite
                if sprite == 'b':
                    fenetre.blit(brique, (x,y))
                cpt_sprite += 1
                
            cpt_ligne -= 1
            cpt_ligne_inverse += 1


    # test si il y a collision avec une brique
    # si oui destruction de la brique
    # renvoi "nop" si pas de collision
    # renvoi "X" si collision sur droite ou gauche
    # renvoi "Y" si collision sur haut ou bas
    def collide_brique(self, pos_x , pos_y , nb_ligne):
        if (pos_y > ((15+(30*nb_ligne)+30))) :
            return "nop"
        collide_x = pos_x +20 #reajustement de la hitbox
        collide_y = pos_y +45
        nbLigne = nb_ligne
        i=0
        j=0
        for ligne in self.structure :
            for brique in ligne :
                if brique == 'b' :
                    if (collide_y > (15+(30*nbLigne))) and (collide_y < ((15+(30*nbLigne)+30))):
                        if (collide_x > (15+(30*j))) and (collide_x < ((15+(30*j))+30)) :
                            #suppression de la brique
                            self.structure[i][j] = 'n'
                            # test du lieu de collision
                            top = (15+(30*nbLigne))
                            bottom = (15+(30*nbLigne)+30)
                            left = (15+(30*j))
                            if collide_y > (bottom-3) :
                                return "Y"
                            elif collide_y < (top+3) :
                                return "Y"
                            elif collide_x < (left+3) :
                                return "X"
                            else :
                                return "X"
                j+=1
            i+=1
            j=0                
            nbLigne -= 1
        return "nop"
    
    #test si l'utilisateur à gagné
    # signifie qu'il n'y a que des "n" dans self.structure
    def win(self) :
        for ligne in self.structure :
            for brique in ligne :
                if brique == 'b' :
                    return False      
        return True
        
