#Faça um programa em Python que abra
# e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
#screen = pygame.display.set_mode((640, 480))
pygame.mixer.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()





