from constant import *
from classes import *

def appear_hero(zone, hero, pos):
    zone.layout[pos[0]][pos[1]].hasHero = True
    zone.layout[pos[0]][pos[1]].hero = hero
    hero.pos = pos
    zone.heroes.append(hero)
