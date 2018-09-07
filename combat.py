from classes import *
from constant import *
from hero_creation import *
from pygame.locals import *
import pygame
import math
import copy

def effective_damage(attacker, defender):
    if attacker.wpnType == BOW and defender.mvtType == FLYING:
        return True
    return False

def true_damage(attacker, defender):
    actual_atk = attacker.ATK + attacker.weapon.might
    if effective_damage(attacker, defender) == True:
        actual_atk = math.floor(attacker.ATK + (attacker.ATK / 2))

    if attacker.wpnType < BREATH or attacker.wpnType == BOW:
        defender.HP -= actual_atk - defender.DEF
    else:
        defender.HP -= actual_atk - defender.RES

    if defender.HP <= 0:
        defender.HP = 0
        defender.isAlive = False

def mock_battle(attacker, defender):
    attackertmp = copy.deepcopy(attacker)
    defendertmp = copy.deepcopy(defender)

    if (attacker.SPD >= defender.SPD + 5):
        nbattacker = 2
    else:
        nbattacker = 1
    if (defender.SPD >= attacker.SPD + 5):
        nbdefender = 2
    else:
        nbdefender = 1

    attackorder = []
    while nbattacker > 0 or nbdefender > 0:
        if (nbattacker > 0):
            attackorder.append(1)
            nbattacker -= 1
        if (nbdefender > 0):
            attackorder.append(2)
            nbdefender -= 1

    for fighter in attackorder:
        if fighter == 1:
            true_damage(attacker, defender)
            if defender.isAlive == False:
                return (attacker, defender)
        if fighter == 2:
            true_damage(defender, attacker)
            if attacker.isAlive == False:
                return (attacker, defender)
        print(attacker.HP, defender.HP)

    return attacker, defender
