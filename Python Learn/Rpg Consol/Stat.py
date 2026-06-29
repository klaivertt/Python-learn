#Max value for rpg stat
MAX_STAT = 20

class Stat:
    def __init__(self):
        # Health
        self.health = 0
        self.healthRegeneration = 0
        
        #Rpg stat
        self.strength = 0
        self.dexterity = 0
        self.intelligence = 0
        self.vitality = 0
        self.luck = 0

        # Mana
        self.maxMana = 0
        self.manaRegeneration = 0

        # Damage
        self.attackDamage = 0
        self.attackSpeed = 0.0

        # Armor
        self.armor = 0
        self.magicResistance = 0

        # Critical damage
        self.criticalChance = 0.0
        self.criticalDamage = 0.0

        # life steal
        self.lifeSteal = 0

        # Precision
        self.accuracy = 0
        self.dodge = 0

        # Penetration
        self.armorPenetration = 0
        self.magicPenetration = 0