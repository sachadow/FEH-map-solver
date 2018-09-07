from classes import *
from constant import *
from hero_creation import *
from combat import *
from pygame.locals import *
import pygame

def movement_range(zone, hero):
    if (hero.mvtType == INFANTRY):
        mvtRange = 2
        mvCost = [0, 1, 2, 10, 1, 10]
    elif (hero.mvtType == FLYING):
        mvtRange = 2
        mvCost = [0, 1, 1, 1, 1, 10]
    elif (hero.mvtType == CAVALRY):
        mvtRange = 3
        mvCost = [0, 1, 10, 10, 3, 10]
    else:
        mvtRange = 1
        mvCost = [0, 1, 1, 10, 1, 10]

    a = 0
    x = 0
    valid_rangex = [hero.pos[0]]
    valid_rangey = [hero.pos[1]]
    valid_range = [mvtRange]
    prev_range = []
    move_x = [1, -1, 0, 0]
    move_y = [0, 0, 1, -1]
    while (a == 0 or valid_range != prev_range):
        prev_range = valid_range
        a += 1
        i = 0
        for vrange in valid_range:
            if (vrange > 0):
                for x in range(0, 4):
                    if (valid_rangex[i] + move_x[x] <= 5 and valid_rangex[i] + move_x[x] >= 0 and
                            valid_rangey[i] + move_y[x] <= 7 and valid_rangey[i] + move_y[x] >= 0 and
                            vrange - mvCost[zone.layout[valid_rangex[i] + move_x[x]][valid_rangey[i]
                            + move_y[x]].tilemove] >= 0):
                        i2 = 0
                        ok = False
                        for vrange2 in prev_range:
                            if not (vrange == vrange2 and [valid_rangex[i] + move_x[x],
                                valid_rangey[i] + move_y[x]] == [valid_rangex[i2], valid_rangey[i2]]):
                                ok = True
                            i2 += 1
                        if (ok == True):
                            valid_rangex.append(valid_rangex[i] + move_x[x])
                            valid_rangey.append(valid_rangey[i] + move_y[x])
                            valid_range.append(vrange -
                                    mvCost[zone.layout[valid_rangex[i] + move_x[x]][valid_rangey[i]
                                    + move_y[x]].tilemove])
            i += 1
    return (valid_rangex, valid_rangey)


def can_go_there(zone, hero, pos):

    if (zone.layout[pos[0]][pos[1]].hasHero == True):
        return (False)

    rangex, rangey = movement_range(zone, hero)
    for i in range(len(rangey)):
        if (rangex[i] == pos[0] and rangey[i] == pos[1]):
            return (True)
    return (False)


def threaten_range(zone, hero):
    rangex, rangey = movement_range(zone, hero)
    print(rangex)
    print(rangey)
    attackx = []
    attacky = []
    if (hero.weapon.name == "none"):
        return (attackx, attacky)
    if (hero.wpnType <= BREATH):
        atkRangex = [1, -1, 0, 0]
        atkRangey = [0, 0, 1, -1]
    else:
        atkRangex = [2, -2, 0, 0, 1, 1, -1, -1]
        atkRangey = [0, 0, 2, -2, 1, -1, 1, -1]
    i = 0
    a = 0
    b = 0
    for i in range(len(rangex)):
        for a in range(len(atkRangex)):
            ok = True
            if (rangex[i] + atkRangex[a] >= 0 and rangex[i] + atkRangex[a] <= 5 and
                    rangey[i] + atkRangey[a] >= 0 and rangey[i] + atkRangey[a] <= 7):
                for b in range(len(attackx)):
                    if (rangex[i] + atkRangex[a] == attackx[b] and rangey[i] + atkRangey[a] == attacky[b]):
                        ok = False
                if (ok == True):
                    attackx.append(rangex[i] + atkRangex[a])
                    attacky.append(rangey[i] + atkRangey[a])
    return (attackx, attacky)


def print_map(zone, window):
    a = 0
    rangex, rangey = threaten_range(zone, zone.heroes[0])
    i = 0
    for a in rangex:
        b = rangey[i]
        rect = Rect(5 + (a * (HEIGHT / 8)), 5 + (b * (HEIGHT / 8)),
            HEIGHT / 8, HEIGHT / 8)
        pygame.draw.rect(window, (150, 0, 150, 122), rect)
        i += 1
    a = 0
    for line in zone.layout:
        b = 0
        for tile in line:
            if zone.layout[a][b].tilemove == PLAIN:
                color = Color(0, 230, 0)
            elif zone.layout[a][b].tilemove == FOREST:
                color = Color(0, 122, 30)
            elif zone.layout[a][b].tilemove == MOUNTAIN:
                color = Color(200, 200, 0)
            elif zone.layout[a][b].tilemove == TRENCH:
                color = Color(50, 150, 150)
            else:
                color = Color(30, 30, 30)
            rect = Rect(10 + (a * (HEIGHT / 8)), 10 + (b * (HEIGHT / 8)),
                HEIGHT / 8 - 10, HEIGHT / 8 - 10)
            pygame.draw.rect(window, color, rect)
            if zone.layout[a][b].hero != 0:
                if (zone.layout[a][b].hero.alignment == True):
                    color = Color(0, 0, 255)
                else:
                    color = Color(255, 0, 0)
                pygame.draw.ellipse(window, color, rect)
            b += 1
        a += 1


def init_tiles(zone):
    zone.layout[2][1].tilemove = MOUNTAIN
    zone.layout[2][2].tilemove = FOREST
    zone.layout[1][2].tilemove = TRENCH
    zone.layout[3][3].tilemove = FOREST
    zone.layout[4][2].tilemove = FOREST
    zone.layout[1][4].tilemove = FOREST
    zone.layout[1][5].tilemove = FOREST
    zone.layout[2][4].tilemove = FOREST

    hero = Hero(True, [0, 0], 'marth', 40, 40, 32, 32, 30, 21, 0, 0, 0, 0, Weapon("no", 16))
    hero2 = Hero(True, [0, 0], 'Marth', 40, 40, 32, 32, 30, 21)
    attacker, defender = mock_battle(hero, hero2)
    appear_hero(zone, hero, [2, 2])
    print(zone.heroes[0].pos)

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
