from Entity import Entity
from Stat import Stat
import Tools

XP_REQUIRED_BY_LEVEL = 30

class Player(Entity):
    def __init__(self):
       super().__init__()
       
       self.strength = 7
       self.dexterity = 7
       self.intelligence = 7
       self.vitality = 7
       self.luck = 7
       
       self.baseStat = Stat(_health = 610, _healthRegeneration = 3.5,_maxMana = 280, _manaRegeneration = 7, _attackDamage = 59, _armor = 26, _magicResistance = 30, _criticalDamage = 1.25)
       
       self.statByLevel = Stat(_health = 101, _healthRegeneration = 0.55, _maxMana = 35, _manaRegeneration = 0.65, _attackDamage = 3.5, _armor = 4.6, _magicResistance = 1.3)
       
    def SetName(self):
        while True:
            try:
                name = str(input("Enter your name : ").strip().title())
                break
            except ValueError:
                print("Please enter an valid string for your name")
        
        self.name = name
        
    def StatisticalDistribution(self, _nb):
        # stat a repartir 
        # boucle while tant que player a des stat a repartir
        # demander valeur au joeur a repartir dans les différente categorie
        # si valeur mauvaise recomancer la boucle interne sinon decremanter -> stat a repartir tant que stat a repartir au desus de zero alors 
        # continuer la repartition
        # ne pas oublier de verrifier que le joeur peux s'attribuer ses stat ou non stat a repartir >= stat choisit par joeur 
        # verifier aussi que la stat ne depasse pas la stat maximum de cette categorie
        
        point = _nb
        actions = ['[S]trength', '[D]exterity', '[I]ntelligence','[V]itality', '[L]uck']
       
        choice = ""
        
        while point > 0:
            Tools.ClearS()
            self.DisplayAbility()
            
            while True:
                
                attribute = Tools.AskChoice("Choose an attribute to assign a point : ", actions)
                
                if attribute in ("s","strength"):
                    choice =  "strength"
                    break
                elif attribute in ("d","dexterity"):
                    choice =  "dexterity"
                    break
                elif attribute in ("i","intelligence"):
                    choice =  "intelligence"
                    break
                elif attribute in ("v","vitality"):
                    choice =  "vitality"
                    break
                elif attribute in ("l","luck"):
                    choice =  "luck"                
                    break
                else :
                    print("Please enter an valid attribute between '[S]trength', '[D]exterity', '[I]ntelligence','[V]itality', '[L]uck' ")
            
            attributed = True
            
            if choice == "strength":
                if self.strength < 15:
                    self.strength += 1
                else:
                    attributed = False
            if choice == "dexterity":
                if self.dexterity < 15:
                    self.dexterity += 1
                else:
                    attributed = False
            if choice == "intelligence":
                if self.intelligence < 15:
                    self.intelligence += 1
                else:
                    attributed = False
            if choice == "vitality":
                if self.vitality < 15:
                    self.vitality += 1
                else:
                    attributed = False
            if choice == "luck":
                if self.luck < 15:
                    self.luck += 1
                else:
                    attributed = False
            
            if not attributed:
                print(f"You can't attribute more than 15 to an ability")
            else :
                print(f"1 point assigned to {choice}.")        
                print(f"Point left to attribute {point}")
                
                point -= 1
            
    def DisplayAbility(self):
        Tools.PrintSubTitle("Ability")
        
        print()
        displayed = {"Strength" : self.strength,"Dexterity" : self.dexterity, "Intelligence" : self.intelligence,"Vitality": self.vitality, "Luck" : self.luck}
        
        for name in displayed:
            print(f"{name:>15} : {displayed[name]}")

        print("_"*25)
        
     
    def EarnXp(self, _xpValue):
        self.xp += _xpValue
        
        if(self.IsLevelUp()):
            self.LevelUp()
        
    def LevelUp(self):
        #appliquer des modification sur les level stat du player
        Tools.PrintSubTitle(f"You've levelled up to level : {self.level} !!")
        
        print("You earn 1 attribute point")
        self.StatisticalDistribution(1)
        
        self.AddBaseToStat()
        
        self.xp -= self.GetRequiredXp()
        self.level += 1

        
    def GetRequiredXp(self):
        nextLevel = self.level + 1
        xpSquared = (XP_REQUIRED_BY_LEVEL * (nextLevel - 1)) * (XP_REQUIRED_BY_LEVEL * (nextLevel - 1))
       
        return 20 + xpSquared
        
            
    def IsLevelUp(self):
        #verifier si l'xp gagner > a 20+30*(x-1)^2
        #si oui retourner vrai sion toujour retourner faux       
       
        if self.xp >= self.GetRequiredXp():
            return True
        
        return False