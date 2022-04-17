'''Faça um programa no python que abra e reproduza um arquivo de mp3!'''

import pygame

pygame.init()
pygame.mixer.music.load('de21.mp3.mp3')
pygame.mixer.music.play()
pygame.event.wait()

from playsound import playsound

playsound('de21.mp3.mp3')

input('tecle algo para encerrar!')

