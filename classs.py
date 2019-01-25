import pygame
from pygame.locals import*

class Niveau :

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        with open(self.fichier, "r") as fichier
            structure_niveau =[]

            for ligne in fichier :
                ligne_niveau = []

                for brique in ligne :
                    if brique != '\n':
                        ligne_niveau.append(sprite)

                    structure_niveau.append(ligne_niveau)

            self.structure = structure_niveau

    def affiche_ligne(self, fenetre,num_ligne):
        brique = pygame.image.load("mur.png")
        num_ligne= num_ligne - 1
        y = 15 + 30*num_ligne
        cpt_ligne = 0
        for ligne in self.structure:
            if num_ligne == cpt_ligne :
                cpt_sprite = 0
                for sprite in ligne:
                    x = 15 + 30*cpt_sprite
                    if sprite == 'b':
                        fenetre.blit(brique, (x,y))
                    cpt_sprite += 1
                
            cpt_ligne += 1

