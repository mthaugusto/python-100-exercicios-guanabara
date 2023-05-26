# [21 / 100] Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Importar a biblioteca pygame - caso não esteja instalada, digitar pip install pygame no console
import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar o arquivo MP3
pygame.mixer.music.load("C:\\Users\\mthau\\Desktop\\Gustav Holst - The Planets - Mars, the Bringer of War.mp3")

# Reproduzir o arquivo MP3
pygame.mixer.music.play()

# Manter o programa em execução enquanto a música está tocando
while pygame.mixer.music.get_busy():
    continue