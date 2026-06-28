class Stat :
    def __init__(self):
        self.healthRegeneration = float(1)
        self.armor = 20
        self.magicResistance = 25
        self.attackSpeed = float(0.8)
        self.attackDamage = 15
        self.abilityPower = 18
        self.criticalStrikeChance = float(0)
        self.criticalStrikeDamage = float(0.25)
        self.armorPenetration = 0
        self.magicPenetration = 0

class Player :
    def __init__(self):
        self.name = ""
        self.health = 20
        self.maxHealth = self.health
        self.level = 1
        self.xp = 0
        self.gold = 0
        
        