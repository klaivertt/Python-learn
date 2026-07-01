
class Stat:
    def __init__( self, 
        _health=0, 
        _healthRegeneration = 0.0,
        _maxMana=0,
        _manaRegeneration=0.0,
        _attackDamage=0.0,
        _magicDamage = 0.0,
        _armor=0.0,
        _magicResistance=0.0,
        _criticalChance=0.0,
        _criticalDamage = 0.0,
        _lifeSteal=0.0,
        _armorPenetration=0.0,
        _magicPenetration=0.0,
    ):
        self.health = _health
        self.healthRegeneration = _healthRegeneration

        self.maxMana = _maxMana
        self.manaRegeneration = _manaRegeneration

        self.attackDamage = _attackDamage
        self.magicDamage = _magicDamage

        self.armor = _armor
        self.magicResistance = _magicResistance

        self.criticalChance = _criticalChance
        self.criticalDamage = _criticalDamage

        self.lifeSteal = _lifeSteal

        self.armorPenetration = _armorPenetration
        self.magicPenetration = _magicPenetration