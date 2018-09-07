from constant import *

class Skill:

    def __init__(self, name = "none", level = 1, slot = 0):
        self.name = name
        self.level = level
        self.slot = slot

class Weapon:

    def __init__(self, name = "none", might = 0, effect = []):
        self.name = name
        self.might = might
        self.effect = effect

class Assist:

    def __init__(self, name = "none"):
        self.name = name

class Special:

    def __init__(self, name = "none", CD = 0):
        self.name = name
        self.CD = CD

class Map:

    def __init__(self, layout = [], name = "default", heroes = []):
        self.layout = layout
        self.name = name
        self.heroes = heroes

class Tile:

    def __init__(self, tilemove = PLAIN, fort = False, trench = False, hp = 0,
            hasHero = False, hero = 0):
        self.tilemove = tilemove
        self.fort = fort
        self.trench = trench
        self.hp = hp
        self.hasHero = hasHero
        self.hero = hero

    def takeDmg(self):
        self.hp -= 1
        if self.hp < 0:
            self.hp = 0

class Hero:
    
    def __init__(self, alignment = True, pos = [0, 0],
            name = "Marth", maxHP = 40, HP = 40, ATK = 32,
            SPD = 32, DEF = 30, RES = 21, skillA = Skill(), skillB = Skill(),
            skillC = Skill(), skillS = Skill(),
            weapon = Weapon(), assist = Assist(), special = Special(),
            mvtType = INFANTRY, wpnType = SWORD, color = RED,
            CD = 0, isAlive = True, panicStatus = False, candleStatus = False, TAStatus = False,
            gravityStatus = False, ATKbuff = 0, SPDbuff = 0, DEFbuff = 0, RESbuff = 0):
        self.alignment = alignment
        self.name = name
        self.pos = pos
        self.maxHP = maxHP
        self.HP = HP
        self.ATK = ATK
        self.SPD = SPD
        self.DEF = DEF
        self.RES = RES
        self.BST = ATK + SPD + DEF + RES + maxHP
        self.skillA = skillA
        self.skillB = skillB
        self.skillC = skillC
        self.skillS = skillS
        self.weapon = weapon
        self.assist = assist
        self.special = special
        self.mvtType = mvtType
        self.wpnType = wpnType
        self.color = color
        self.gravityStatus = gravityStatus
        self.panicStatus = panicStatus
        self.candleStatus = candleStatus
        self.TAStatus = TAStatus
        self.ATKbuff = ATKbuff
        self.SPDbuff = SPDbuff
        self.DEFbuff = DEFbuff
        self.RESbuff = RESbuff
        self.CD = CD
        self.isAlive = isAlive

    def takeDmg(self, damage):
        self.HP -= damage
        if self.HP <= 0:
            isAlive = False
