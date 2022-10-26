import pygame
from pygame.locals import *

pygame.init()

running = True
pygame.display.set_caption("Alquerque")
hauteur = 715
largueur = 600
alquerque = pygame.display.set_mode((hauteur,largueur))

def InitBoard():
    plateau = pygame.image.load('C:/Users/mathi/Documents/COURS/1PROJ RATTRAPAGE/alquerqueBoard.png').convert()
    plateau_rect = plateau.get_rect(center=(358, 300))
    alquerque.blit(plateau, plateau_rect)

    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if Board[i][j].image is not None:
                Board[i][j].rect = Board[i][j].image.get_rect(center=(160 * (j+0.24),125 * (i+0.40)))
                if Board[i][j].joueur != 0:
                    alquerque.blit(Board[i][j].image, Board[i][j].rect)
    pygame.display.update()


class pion(pygame.sprite.Sprite):
    def __init__(self,joueur):
        super().__init__()
        self.joueur = joueur
        self.image = None
        if joueur == 1:
            self.image = pygame.transform.scale(pygame.image.load("C:/Users/mathi/Documents/COURS/1PROJ RATTRAPAGE/pionblanc.png"),(50,50))
        elif joueur == 2:
            self.image = pygame.transform.scale(pygame.image.load("C:/Users/mathi/Documents/COURS/1PROJ RATTRAPAGE/pionnoir2.png"),(50,50))
        elif joueur == 0:
            self.image = pygame.transform.scale(pygame.image.load("C:/Users/mathi/Documents/COURS/1PROJ RATTRAPAGE/pionnoir2.png"),(50,50))

Board = [[pion(2),pion(2),pion(2),pion(2),pion(2)],
         [pion(2),pion(2),pion(2),pion(2),pion(2)],
         [pion(2),pion(2),pion(0),pion(1),pion(1)],
         [pion(1),pion(1),pion(1),pion(1),pion(1)],
         [pion(1),pion(1),pion(1),pion(1),pion(1)]]




while running:
    InitBoard()
    for event in pygame.event.get():
        running = True
        pygame.display.update()
pygame.quit()
