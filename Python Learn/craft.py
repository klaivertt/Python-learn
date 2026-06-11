def GetInt(_str):
    while True:
        try:
            return int(input(_str))
        except ValueError:
            print("Enter an valid Int")

def CreateItem(_gameData):
    choice = None
    
    print()
    print("--------------------------------------")
    print("Create new Item")
    
    while True:
        choice = input("Do you want create an item? Yes or No: ").strip().lower()
        
        if choice == "Yes" or choice == "No":
            break
        else :
            print("Please enter 'Yes' or 'No'")
    
    if choice == "No":
        return
    
    name = input("Please enter a name for your item : ").strip().lower()
    
    if name in _gameData["item"]:
        print("Item already exists")
        return
    
    _gameData["item"].append(name)
    print(f"{name} was created")     

def RemoveItem(_gameData):
    choice = None
    
    print()
    print("--------------------------------------")
    print("Delete an existing Item")
    
    while True:
        choice = input("Do you want delete an item? Yes or No: ").strip().lower()
         
        if choice == "yes" or choice == "no":
            break
        else :
            print("Please enter 'Yes' or 'No'")
        
    if choice == "no":
        return
    print("What Item you want to remove")
    
    DisplayItem(_gameData)
    
    while True:
        print("if you want cancer please enter 'cancel'")
        itemName = input("Name of item you want to remove :").strip().lower()
        
        if itemName == "cancel":
            return
        
        if itemName in _gameData["item"]:
            del  _gameData["item"].remove(itemName)
        else:
            print("Item doesn't Existe")
    
def DisplayItem(_gameData):
    print("Existing Item")
    print("--------------------------------------")
    for item in _gameData["item"]:
        print(item)

def CreateCraft(_gameData):
    print()
    print("--------------------------------------")
    print("Create a craft")
    
    while True:
        choice = input("Do you want create an Craft? Yes or No: ").strip().lower()
        
        if choice == "Yes" or choice == "No":
            break
        else :
            print("Please enter 'Yes' or 'No'")
    
    if choice == "No":
        return
    
    recipeName = None
    while True:
        recipeName = input("Chose a name for your craft").strip().lower()
        
        print(f"{recipeName} , confirm your craft name")
        print("'Yes' or 'No'")
        
        valid = input("Enter your choice :").strip().lower()
        
        if valid == "yes":
            break
           
    
    DisplayItem(_gameData)
    
    craft = {}
    
    while True:
        print("If you want cancel tape 'Cancel' if your craft is done tape 'Done'")
        print(f"What item you want in your craft: {recipeName}")
        
        itemName = input("Name of the item : ").strip().lower()
        
        if itemName in _gameData["item"]:
            nb = GetInt(f"number of your item: {itemName} you want :")
            if itemName in craft :
                print(f"this item is already in your craft")
                print(f"Do you want add this quantity {nb} of {itemName} in your craft")
                print("'Yes' or 'No'")
                
                valid = input("Enter your choice :").strip().lower()
                
                if valid == "yes":
                    craft[itemName] += nb
            else :
                valid = input("Enter your choice :").strip().lower()
                print(f"Do you want add this quantity {nb} of {itemName} in your craft")
                print("'Yes' or 'No'")
                 
                if valid == "yes":
                    craft[itemName] = nb
        elif itemName == "done":
            break
        elif itemName == "cancel":
            return
        else:
            print("this item doesn't exist")
    
    resultItem = None    
    while True:
        resultItem = input(f"Item you want for result of {recipeName} : ").strip().lower()
        
        if resultItem in _gameData["item"]:
            break
        else:
            print("Please enter an valid item name")
    
    nbResultItem = GetInt(f"How you want {resultItem} for your craft :")
    craft["result"] = {resultItem : nbResultItem}
    _gameData["recipes"][recipeName] = craft

def RemoveCraft(_gameData ):
    print()
    print("--------------------------------------")
    print("Delete an existing Craft")
    
    DisplayItem(_gameData)
    
    name = None
    isvalid = False
    while not isvalid:
        print("if you want cancel enter 'Cancel'")
        name = input("choise an craft to remove it : ")
        
        if name in _gameData["recipes"]:
            while True:
                print(f"Do you want to remove this craft {name}, 'Yes' or 'No'")
                choice = input("Enter your choice :").strip().lower()
                
                if choice == "no":
                    return
                elif choice == "yes":
                    isvalid = True
                    break
                else:
                    print("Please enter 'Yes' or 'No'")
        elif name == "cancel":
            return            
        else:
            print("Please enter an valid item name")
    
    del _gameData["recipes"][name]
            
         

def Craft(_gameData):
    print()
    print("--------------------------------------")
    print("What item you want to craft ?")
    
    DisplayItem(_gameData)
    DisplayInventory(_gameData)
    
    craftName = None 
    while True:
        craftName = input("Enter the craft name : ")
        
        if craftName in _gameData["recipes"]:
            break
        else:
            print("Please enter an valid Craft name")
    
    print(f"To craft {craftName} you need :")
    for item in _gameData["recipes"][craftName]:
        print(item, ":", _gameData["recipes"][craftName][item])
    
    for item in _gameData["recipes"][craftName]:
        if item in _gameData["inventory"]:
            print(f"You have {item} : {_gameData["inventory"][item]} in your inventory")
    
    while True:
        choice = input(f"Do you want Craft {craftName}? Yes or No: ").strip().lower()
         
        if choice == "yes" or choice == "no":
            break
        else :
            print("Please enter 'Yes' or 'No'")
    craftValid = True
    
    for item in _gameData["recipes"][craftName]:
        if _gameData["recipes"][craftName][item] > _gameData["inventory"][item]:
            craftValid = False
   
    if craftValid:
        for item in _gameData["recipes"][craftName]:
           _gameData["inventory"][item] -= _gameData["recipes"][craftName][item]
           print(f"{_gameData["recipes"][craftName][item]} {item} are removed ")
    else:
        print("You don't have enough resources")
        return
    
    if _gameData["recipes"][craftName]["result"] in _gameData["inventory"] :
        _gameData["inventory"][_gameData["recipes"][craftName]["result"]] += _gameData["recipes"][craftName]["result"][]
    else:
        _gameData["inventory"][_gameData["recipes"][craftName]["result"]] = 1
        
    print(f"{craftName} are added to your inventory")
        
    
        

def DisplayInventory(_gameData):
    for item in _gameData["inventory"]:
        print(item, ":", _gameData["inventory"][item])
    
def GetMenuAction(_menu, _str):
    print("Navigate into menu choice:")
    for menu in _menu:
        print(menu, " | ", end="")
    
    print()
    while True:
        choisse = input(_str).strip().lower()
        if choisse in _menu:
            return choisse
        else:
            print("Name of menu unknown please retry")

def main():
    gameData = {
    "inventory": {},
    "recipes": {},
    "item" : []
    }
    
    menuAction = {
        "create item": CreateItem,
        "remove item": RemoveItem,
        "display item": DisplayItem,
        "create craft": CreateCraft,
        "remove craft": RemoveCraft,
        "display inventory": DisplayInventory,
        "craft" : Craft,
        "quit" : None
    }
    
    while True:
        print()
        print("----------------------------------------------")
        print()
        
        choice = GetMenuAction(menuAction, "Select an action : ")
        
        if choice == "quit":
            break
        
        if choice in menuAction:
            menuAction[choice](gameData)
    
    
        