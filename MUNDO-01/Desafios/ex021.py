# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3


import pygame
pygame.init()
pygame.mixer.music.load('Desafios/ex021.mp3.wav')
pygame.mixer.music.play()
pygame.time.wait(10000)
pygame.mixer.music.stop()


