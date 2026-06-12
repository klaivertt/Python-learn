def GetInt(_str):
    while True:
        try:
            return int(input(_str))
        except ValueError:
            print("Enter an valid Int")

def YesNo(_str):
    while True:
        choice = input(_str).strip().lower()
        
        if choice == "yes" or choice == "no":
            return choice
        else :
            print("Please enter 'Yes' or 'No'")    

def CreateItem(_gameData):
    choice = None
    
    print()
    print("--------------------------------------")
    print("Create new Item")
    
    DisplayInventory(_gameData)
    
    choice = YesNo("Do you want create an item? Yes or No: ")      
    
    if choice == "no":
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
    
    DisplayInventory(_gameData)
    
    choice = YesNo("Do you want delete an item? Yes or No: ")
        
    if choice == "no":
        return
    print("What Item you want to remove")
    
    DisplayItem(_gameData)
    
    while True:
        print("if you want cancel please enter 'cancel'")
        print("if you remove an item this item is removed in your inventory to")
        itemName = input("Name of item you want to remove :").strip().lower()
        
        if itemName == "cancel":
            return
        
        if itemName in _gameData["item"]:
            _gameData["item"].remove(itemName)
            
            if itemName in _gameData["inventory"]:
               del _gameData["inventory"][itemName]
            break
        else:
            print("Item doesn't Existe")
    
def DisplayItem(_gameData):
    print()
    print("Existing Item")
    print("--------------------------------------")
    for item in _gameData["item"]:
        print(item)

def CreateCraft(_gameData):
    print()
    print("--------------------------------------")
    print("Create a craft")
    
    choice = YesNo("Do you want create an Craft? Yes or No: ")
        
    if choice == "no":
        return
    
    recipeName = None
    while True:
        recipeName = input("Chose a name for your craft : ").strip().lower()
        
        valid = YesNo(f"{recipeName} , confirm your craft name. 'Yes' or 'No'")
        
        if valid == "yes":
            break
    
    DisplayItem(_gameData)
    
    craft = {}
    
    while True:
        print()
        print("If you want cancel tape 'Cancel' if your craft is done tape 'Done'")
        print(f"What item you want in your craft: {recipeName}")
        
        itemName = input("Name of the item : ").strip().lower()
        
        if itemName in _gameData["item"]:
            nb = GetInt(f"number of your item: {itemName} you want :")
            if itemName in craft :
                print(f"this item is already in your craft")
                print(f"Do you want add this quantity {nb} of {itemName} in your craft")
                                
                valid = YesNo("Enter your choice 'Yes' or 'No':")
                
                if valid == "yes":
                    craft[itemName] += nb
            else :
                print(f"Do you want add this quantity {nb} of {itemName} in your craft")
                
                valid = YesNo("Do you want add this item? 'Yes' or 'No'")
                 
                if valid == "yes":
                    craft[itemName] = nb
        elif itemName == "done":
            break
        elif itemName == "cancel":
            return
        else:
            print("this item doesn't exist")
    
    craft["result"] = {} 
    while True:
        resultItem = None    
        while True:
            resultItem = input(f"Item you want for result of {recipeName} : ").strip().lower()
            
            if resultItem in _gameData["item"]:
                break
            else:
                print("Please enter an valid item name")
    
        nbResultItem = GetInt(f"How many {resultItem} do you want : ")
        craft["result"][resultItem] = nbResultItem
    
        addAnother = YesNo("Do you want to add another item? Yes or No : ")       
    
        if addAnother == "no":
            break

    _gameData["recipes"][recipeName] = craft

def RemoveCraft(_gameData ):
    print()
    print("--------------------------------------")
    print("Delete an existing Craft")
    
    DisplayCraft(_gameData)
    
    name = None
    isvalid = False
    while not isvalid:
        print()
        print("if you want cancel enter 'Cancel'")
        name = input("choose an craft to remove it : ").strip().lower()
        
        if name in _gameData["recipes"]:
                print(f"Do you want to remove this craft {name}, 'Yes' or 'No'")
                choice = YesNo("Enter your choice :")
                
                if choice == "no":
                    return
                else:
                    isvalid = True
                    break
        elif name == "cancel":
            return            
        else:
            print("Please enter an valid item name")
    
    del _gameData["recipes"][name]
    
def DisplayCraft(_gameData):
    print()
    print("Display Craft")
    print("--------------------------------------")
    for recipe in _gameData["recipes"]:
        print("Craft name :",recipe)
        print("item required")
        for item in _gameData["recipes"][recipe]:
            if item != "result":
                print(item, ":", _gameData["recipes"][recipe][item])
        
        print("Result:")
        for resultItem, resultQuantity in _gameData["recipes"][recipe]["result"].items():
                    print(f"  {resultItem}: {resultQuantity}")
        
         

def Craft(_gameData):
    print()
    print("--------------------------------------")
    print("What item you want to craft ?")
    
    DisplayCraft(_gameData)
    DisplayInventory(_gameData)
    
    craftName = None 
    while True:
        print()
        craftName = input("Enter the craft name : ").strip().lower()
        
        if craftName in _gameData["recipes"]:
            break
        else:
            print("Please enter an valid Craft name")
    
    print()
    print(f"To craft {craftName} you need :")
    for item in _gameData["recipes"][craftName]:
        if item != "result":
            print(item, ":", _gameData["recipes"][craftName][item])
    
    print()
    for item in _gameData["recipes"][craftName]:
        if item != "result":
        
            if item in _gameData["inventory"]:
                print(f"You have {item} : {_gameData['inventory'][item]} in your inventory")
    choice = None
    
    print()
    choice = YesNo(f"Do you want Craft {craftName}? Yes or No: ")
            
    if choice == "no":
        return    
    
    craftValid = True
    for item in _gameData["recipes"][craftName]:
        if item != "result":
            if item in _gameData["inventory"] :
                if _gameData["recipes"][craftName][item] > _gameData["inventory"][item]:
                    craftValid = False
                    break
            else:
                break
   
    if craftValid:
        for item in _gameData["recipes"][craftName]:
            if item != "result":
                if item in _gameData["inventory"] :
                    _gameData["inventory"][item] -= _gameData["recipes"][craftName][item]
                    
                    if _gameData["inventory"][item] <= 0:
                        del _gameData["inventory"][item]
                
                    print(f"{_gameData['recipes'][craftName][item]} {item} are removed ")
    else:
        print("You don't have enough resources")
        return
    
    for finalItem in _gameData["recipes"][craftName]["result"]:
        if  finalItem in _gameData["inventory"] :
            _gameData["inventory"][finalItem] += _gameData["recipes"][craftName]["result"][finalItem]
        else:
             _gameData["inventory"][finalItem] = _gameData["recipes"][craftName]["result"][finalItem]
            
    print(f"{craftName} are added to your inventory")
        

def DisplayInventory(_gameData):
    print()
    print("Display Inventory")
    print("--------------------------------------")
    for item in _gameData["inventory"]:
        print(item, ":", _gameData["inventory"][item])
        
    if not _gameData["inventory"]:
        print("Your inventory is empty")
    
    print("Inventory display complete")

def AddItemInventory(_gameData):
    print()
    print("Add Item in Inventory")
    print("--------------------------------------")
    
    DisplayItem(_gameData)
    
    item = None    
    while True:
        print()
        print("If you want cancel tape 'Cancel'")
        item = input("Choose an item to add in your inventory : ").strip().lower()
        if item == "cancel":
            return
        elif item in _gameData["item"]:
            break
        else:
            print("Please choose an valid item")
    
    print(f"Do you want add this item: {item} in your inventory?")
    
    choice = YesNo("'Yes' or 'No' ? ")
    
    if choice == "no":
        return
    
    nb = GetInt(f"Choose a quantity of {item} you want to add in your inventory : ")
    
    if item in _gameData["inventory"]:
        _gameData["inventory"][item] += nb
    else:
        _gameData["inventory"][item] = nb
    
    print(f"{nb} {item} was added in your inventory")
    print(f"You have {_gameData['inventory'][item]} {item}")

def RemoveItemInventory(_gameData):
    print()
    print("Remove Item in Inventory")
    print("--------------------------------------")
    
    DisplayItem(_gameData)
    
    while True:
        print("If you want cancel tape 'Cancel'")
        item = input("Choose an item to remove in your inventory : ").strip().lower()
        
        if item == "cancel":
            return
        elif  item in _gameData["item"]:
            break
        else:
            print("Please choose an valid item")
    
    if item not in _gameData["inventory"]:
        print(f"This item:{item} wasn't present in your inventory")
        return
    
    print(f"Do you want remove this item: {item} of your inventory?")
    
    choice = YesNo("'Yes' or 'No' ? ")
    
    if choice == "no":
        return
    
    nb = GetInt(f"Choose a quantity of {item} you want to remove in your inventory : ")
    
    if item in _gameData["inventory"]:
        _gameData["inventory"][item] -= nb
        if _gameData["inventory"][item] <= 0:
            del _gameData["inventory"][item]  
            print(f"{item} was removed of your inventory")
        else:
            print(f"{nb} {item} was removed of your inventory")
            print(f"You have {_gameData['inventory'][item]} {item}")
    

def GetMenuAction(_menu, _str):
    print()
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
        "add item": AddItemInventory,
        "remove item inventory": RemoveItemInventory,
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
        elif choice in menuAction:
            menuAction[choice](gameData)
    
    
main()