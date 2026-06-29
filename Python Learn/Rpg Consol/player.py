from Entity import Entity


class Player(Entity):
    def __init__(self):
       super().__init__()
    
       
       
    
    def SetName(self):
        while True:
            try:
                name = str(input("Enter your name").strip().title())
                break
            except ValueError:
                print("Please enter an valid string for your name")
        
        self.name = name
        
    
    def StatisticalDistribution():
        point = 7
        
        while point > 0
        # stat a repartir 7
        # boucle while tant que player a des stat a repartir
        # demander valeur au joeur a repartir dans les différente categorie
        # si valeur mauvaise recomancer la boucle interne sinon decremanter -> stat a repartir tant que stat a repartir au desus de zero alors 
        # continuer la repartition
        # ne pas oublier de verrifier que le joeur peux s'attribuer ses stat ou non stat a repartir >= stat choisit par joeur 
        # verifier aussi que la stat ne depasse pas la stat maximum de cette categorie
     
    def EarnXp(self, _xpValue):
        ...
        
    def LevelUp(self):
        ...
        #appliquer des modification sur les level stat du player
    
    def IsLevelUp(self):
        ...
        #verifier si l'xp gagner > a 20+30*(x-1)^2
        #si oui retourner vrai sion toujour retourner faux       