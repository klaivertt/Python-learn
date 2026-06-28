class Stat:
    def __init__(self):
        # Health
        self.maxHealth = 100
        self.health = self.maxHealth
        self.healthRegeneration = 1
        
        #Rpg stat
        self.strength = 10
        self.dexterity = 10
        self.intelligence = 10
        self.vitality = 10
        self.luck = 10

        # Mana
        self.maxMana = 50
        self.manaRegeneration = 1

        # Damage
        self.attackDamage = 15
        self.attackSpeed = 1.0

        # Armor
        self.armor = 20
        self.magicResistance = 20

        # Critical damage
        self.criticalChance = 0.05
        self.criticalDamage = 1.5

        # life steal
        self.lifeSteal = 0

        # Precision
        self.accuracy = 100
        self.dodge = 0

        # Penetration
        self.armorPenetration = 0
        self.magicPenetration = 0