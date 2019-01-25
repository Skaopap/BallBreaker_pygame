import pygame
from pygame.locals import*
from sense_hat import SenseHat 

# Fonctions
def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True

def moveRasp():
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    # Arrondis
    pitch = round(pitch,1)
    roll = round(roll,1)
    # Ajustement des valeurs
    if (pitch>=60 and pitch<=180):
        pitch = 60
    if (pitch>=180 and pitch<=300):
        pitch = 300
    if (roll>=60 and roll<=180):
        roll = 60
    if (roll>=180 and roll<=300):
        roll = 300
    return pitch, roll

# Appel de pygame
pygame.init()

# Appel du sense hat
sense = SenseHat()
sense.set_imu_config(False, True, True)

# Creation de la fenetre
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

# Chargement de l'image de fond, accessible via fond
fond = pygame.image.load("smile.jpg").convert()
fenetre.blit(fond, (0,0))

# raffraichissement
pygame.display.flip()

# chargement du perso / convert_alpha pour transparence
perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
position_perso = position_perso.move(280,180)
fenetre.blit(perso, position_perso)

# Chargement de la brique
brique = pygame.image.load("brique.png").convert_alpha()
position_brique = brique.get_rect()
position_brique = position_brique.move(150,0)
fenetre.blit(brique, position_brique)

# raffraichissement
pygame.display.flip()

continuer = 1

pygame.key.set_repeat(400, 30)
#boucle infinie
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        else:
            while True:
                pitch, roll = moveRasp()           
                if (pitch>=280 and pitch<350):
                    p = 360-pitch
                    speedP = round((p-10)/10)
                    position_perso = position_perso.move(0,-speedP)
                    
                if (pitch>10 and pitch<=80):
                    speedP = round((pitch-10)/10)
                    position_perso = position_perso.move(0,speedP)
                    
                if (roll>10 and roll<=80):
                    speedR = round((roll-10)/10)
                    position_perso = position_perso.move(-speedR,0)
                    
                if (roll>=280 and roll<350):
                    r = 360-roll
                    speedR = round((r-10)/10)
                    position_perso = position_perso.move(speedR,0)
            
                #recollage
                fenetre.blit(fond, (0,0))
                fenetre.blit(brique, position_brique)
                fenetre.blit(perso, position_perso)
                #Raffraichissement
                pygame.display.flip()

# fermeture de pygame
pygame.quit()
            

