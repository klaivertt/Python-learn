from Entity import Entity

XP_REQUIRED_BY_LEVEL = 30

class Player(Entity):
    def __init__(self):
       super().__init__()
       
       self.strength = 7
       self.dexterity = 7
       self.intelligence = 7
       self.vitality = 7
       self.luck = 7
    
    def SetName(self):
        while True:
            try:
                name = str(input("Enter your name").strip().title())
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

        choice = ""
        
        while point > 0:
            while True:
                print("Choose between [S]trength', '[D]exterity', '[I]ntelligence','[V]itality', '[L]uck'")
                attribute = input("Which attribute would you like to assign a point to? ").strip().lower()
                
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
            
            
            if choice == "strength":
                self.strength += 1
            if choice == "dexterity":
                self.dexterity += 1
            if choice == "intelligence":
                self.intelligence += 1
            if choice == "vitality":
                self.vitality += 1
            if choice == "luck":
                self.luck += 1
            print(f"1 point assigned to {choice}.")        
            
            point -= 1
            
       
     
    def EarnXp(self, _xpValue):
        self.xp += _xpValue
        
        if(self.IsLevelUp()):
            self.LevelUp()
        
    def LevelUp(self):
        ...
        #appliquer des modification sur les level stat du player
    
    def IsLevelUp(self):
        ...
        #verifier si l'xp gagner > a 20+30*(x-1)^2
        #si oui retourner vrai sion toujour retourner faux       
        nextLevel = self.level + 1
        
        if self.xp >= (20+ (XP_REQUIRED_BY_LEVEL(nextLevel - 1) * XP_REQUIRED_BY_LEVEL(nextLevel - 1))):
            return True
        
        return False