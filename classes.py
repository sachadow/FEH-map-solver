class Hero:
    
    def __init__(self, alignment = True, name = "Marth", maxHP = 40, HP = 40, ATK = 32,
            SPD = 32, DEF = 30, RES = 21, skillA = 0, skillB = 0, skillC = 0, skillS = 0,
            weapon = 0, assist = 0, special = 0, mvtType = 0, wpnType = 0, color = 0,
            CD = 0, isAlive = True, panicStatus = 0, candleStatus = 0, TAStatus = 0,
            ATKbuff = 0, SPDbuff = 0, DEFbuff = 0, RESbuff = 0):
        self.name = name
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
            

class Map:

    def __init__(self, layout = [], name = "default"):
        self.layout = layout
        self.name = name

class Tile:

    def __init__(self, tilemove = "plain", fort = False, trench = False, hp = 0,
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
