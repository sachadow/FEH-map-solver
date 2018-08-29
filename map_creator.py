from classes import *
from constant import *
from pygame.locals import *
import pygame

def print_map(zone, window):
    a = 0
    for line in zone.layout:
        b = 0
        for tile in line:
            if zone.layout[a][b].tilemove == 'plain':
                color = Color(0, 255, 255)
            elif zone.layout[a][b].tilemove == 'forest':
                color = Color(255, 255, 0)
            else:
                color = Color(255, 0, 0)
            rect = Rect(10 + (a * (HEIGHT / 8)), 10 + (b * (HEIGHT / 8)),
                HEIGHT / 8 - 10, HEIGHT / 8 - 10)
            pygame.draw.rect(window, color, rect)
            if zone.layout[a][b].hero != 0:
                pygame.draw.ellipse(window, (0, 0, 0, 0), rect)

            b += 1
        a += 1

def init_tiles(zone):
    zone.layout[2][1].tilemove = "forest"
    zone.layout[2][2].tilemove = "forest"
    zone.layout[1][2].tilemove = "forest"
    zone.layout[3][3].tilemove = "forest"
    zone.layout[4][2].tilemove = "forest"
    zone.layout[1][4].tilemove = "forest"
    zone.layout[1][5].tilemove = "forest"
    zone.layout[2][4].tilemove = "forest"

    zone.layout[1][2].hero = Hero()

def init_map(window):
    zone = Map()
    a = 0
    b = 0
    while a < 6:
        b = 0
        line = []
        while b < 8:    
            line.append(Tile())
            b += 1
        zone.layout.append(line)
        a += 1
    init_tiles(zone)
    print_map(zone, window)
