import random

def LoadItem():
    loot = []
    for _ in range(random.randint(1, 40)) :
        
        rng = random.randint(0,2)
        # print(rng)
        if rng == 2 :
            loot.append("wood")
        elif rng == 1:
            loot.append("stone")
        else :
            loot.append("iron")
            
    return loot

def CountInvetory(_inventory) :
    inventoryDic = {}
    
    for item in _inventory :
        if item in inventoryDic :
            inventoryDic[item] += 1
        else :
            inventoryDic[item] = 1
    
    return inventoryDic

def main() :
    
    loot = LoadItem()
    
    inventory = CountInvetory(loot)
    
    key = ""
    for item in inventory :
        if key == "" :
            key = item
        elif inventory[item] > inventory[key] :
            key = item  
        
        print(item, inventory[item])
        
    #most collected resource
    print ("Most collected ressource :", key, inventory[key])
        
        
main()