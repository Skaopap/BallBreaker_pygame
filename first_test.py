import pygame
from pygame.locals import*
from random import randrange

from classes import *

# Appel de pygame
pygame.init()
#Creation de la fenetre
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

# chargement de l'image de fond, accessible via fond
fond = pygame.image.load("smile.jpg").convert()
position_fond = fond.get_rect()
fenetre.blit(fond, (0,0))

# raffraichissement
pygame.display.flip()

#chargement des images pour le nb de PV
zero = pygame.image.load("0.png").convert_alpha()
un =  pygame.image.load("1.png").convert_alpha() # pas png à modif
deux = pygame.image.load("2.png").convert_alpha()
trois = pygame.image.load("3.png").convert_alpha()

#chargement de l'image de mort
dead = pygame.image.load("end.png").convert_alpha()
position_dead = dead.get_rect()
position_dead = position_dead.move(130,50)

#chargement de l'image de win
winn = pygame.image.load("win.png").convert_alpha()
position_win = winn.get_rect()
position_win = position_win.move(35,100)

# chargement du perso / convert_alpha pour transparence
perso = pygame.image.load("curseur.png").convert_alpha()
position_perso = perso.get_rect()
position_perso = position_perso.move(150,375)
fenetre.blit(perso, position_perso)

#chargement de la balle pour tirer
balle = pygame.image.load("balle.png").convert_alpha()
position_balle = balle.get_rect()

continuer = 1

nb_ligne = 1 # nb de ligne de brique affiché
nb_dead = 0
tir = False # si le tir est effectué
dead2 = False # si il n'y a plus de vie
dirC = "nop" 

niveau_brique = Niveau("level.txt")
niveau_brique.generer()
niveau_brique.affiche_ligne(fenetre,nb_ligne)

# raffraichissement
pygame.display.flip()

#définition d'évenement recurent
pygame.time.set_timer(pygame.USEREVENT,6000) # event de la descente des briques
pygame.time.set_timer(pygame.USEREVENT +1,12) # event du mouvement de la balle

pygame.key.set_repeat(400, 30)
#boucle infinie
while continuer:
    #limite le raffraichissement
    pygame.time.Clock().tick(30)
    
    for event in pygame.event.get():
        # descente du mur de brique
        if event.type == pygame.USEREVENT:
            if (nb_ligne <=12):
                nb_ligne+=1
        # mouvement de la balle
        if event.type == pygame.USEREVENT+1 and tir :
            position_balle.x += balleRandomX
            position_balle.y += balleRandomY
            #collision avec une brique
            #dirC = "nop"
            dirC = niveau_brique.collide_brique(position_balle.x , position_balle.y , nb_ligne)
           
            #gestion de collision avec les bords ou brique 
            if position_balle.left <= position_fond.left or dirC == "X":
                balleRandomX = -balleRandomX
            if position_balle.right+70 >= position_fond.right  :
                balleRandomX = -balleRandomX
            if position_balle.top <= position_fond.top or dirC=="Y" :
                balleRandomY = -balleRandomY
                
            # Si la balle est perdu
            if not position_balle.colliderect(position_fond) :
                tir = False
                if nb_dead <2:
                    nb_dead += 1
                else :
                    nb_dead += 1
                    dead2 = True

            # Collision avec le curseur 
            if position_balle.colliderect(position_perso) and position_balle.left>=position_perso.left-20:
                balleRandomY = -balleRandomY
                
        if event.type == QUIT:
            continuer = 0

        # Gestion des touches du clavier
        if event.type == KEYDOWN:
            #pour le mouvement du perso
            if event.key == K_DOWN:
                position_perso = position_perso.move(0,15)
            if event.key == K_UP:
                position_perso = position_perso.move(0,-15)
            if event.key == K_RIGHT:
                position_perso = position_perso.move(15,0)
            if event.key == K_LEFT:
                position_perso = position_perso.move(-15,0)
            #pour le tir
            if event.key == K_SPACE :
                if not tir  :
                    balleRandomX = randrange(-5, 5)
                    if balleRandomX < 0 :
                        balleRandomX = 4
                    else :
                        balleRandomX = -2
                    balleRandomY = -3
                    position_balle = position_perso
                    position_balle = position_balle.move(30,-40)
                    tir = True
                            
        #recollage
        fenetre.blit(fond, (0,0))
        # affiche le mur de brique
        niveau_brique.affiche_ligne(fenetre,nb_ligne)
        # affiche le nb de vie
        if tir :
            fenetre.blit(balle, position_balle)
        if nb_dead == 0 :
            fenetre.blit(trois, (0,0))
        elif nb_dead == 1:
            fenetre.blit(deux, (0,0))
        elif nb_dead == 2 :
            fenetre.blit(un, (0,0))
        else :
            fenetre.blit(zero, (0,0))
        # affiche le curseur
        fenetre.blit(perso, position_perso)
        # message de mort
        if dead2 :
            fenetre.blit(dead,position_dead)
        # message de victoire
        if niveau_brique.win() :
            fenetre.blit(winn,position_win)
        #Raffraichissement
        pygame.display.flip()

# fermeture de pygame
pygame.quit()
            

