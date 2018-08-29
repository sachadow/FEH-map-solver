import os
import pygame
from map_creator import *
from constant import *
from pygame.locals import *

def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
    init_map(window)
    end_program = False
    while end_program == False:
        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == QUIT:
                end_program = True
    return (0)

main();
