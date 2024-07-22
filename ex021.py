import pygame

pygame.mixer.init()
pygame.mixer.music.load('som_aviao.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass



