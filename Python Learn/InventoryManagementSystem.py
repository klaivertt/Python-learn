existingItem = []

def GetInt(_str):
    while True:
        try:
            return int(input(_str))
        except ValueError:
            print("Enter an valid Int")


def AddItem(_inventory):

    choice = None
    print()
    print("--------------------------------------")
    print("Create new Item or add an existing item")

    while True:
        choice = input("choisse Create or Add : ").strip().lower()

        if choice == "create" or choice == "add":
            break
        else:
            print("Please write 'Create' or 'Add'")

    if choice == "create":
        name = input("Choisse a name : ").strip().lower()
        if name in existingItem:
            print(f"This item name : {name.title()} already exist")
        else:
            existingItem.append(name)

        nb = GetInt(f"Enter number of {name.title()} you want in your Inventory :")

        _inventory[name] = nb
    elif choice == "add":

        while True:
            print("choose item in")
            for item in existingItem:
                print(item.title())

            name = input("Choisse a item : ").strip().lower()

            if name in existingItem:
                break
            else:
                print("item doesn't exist")

        nb = GetInt(f"Enter number of Item:{name} you want in your Inventory :")
        _inventory[name] += nb

    print("item added")


def RemoveItem(_inventory):
    
    print()
    print("--------------------------------------")
    name = ""
    while True:
        print("choose item in")
        for item in existingItem:
            print(item.title())

        name = input("Choisse a item : ").strip().lower()

        if name in existingItem:
            break
        else:
            print("item doesn't exist")

    
    nb = GetInt(f"Enter number of Item:{name} you want remove in your Inventory : ")
    _inventory[name] -= nb
    
    if _inventory[name] <= 0:
        del _inventory[name]
        print(f"{name} removed from inventory")
            
    print(f"item : {name}: {nb}  removed")


def DisplayInventory(_inventory):    
    print()
    print("--------------------------------------")
    print("You have in your inventory : ")
    for item in _inventory:
        print(item, _inventory[item])
        
    print("inventory display")


def SearchItem(_inventory):
    print()
    print("--------------------------------------")
    name = ""
    while True:
        print("choose item in")
        for item in existingItem:
            print(str(item).title())

        name = input("Choisse a item : ").strip().lower()

        if name in existingItem:
            break
        else:
            print("item doesn't exist")
    
    print(f"You have : {name} = {_inventory[name]}")


def GetMenu(_menu, _str):
    print("Navigate into menu choice: ", end="")
    for menu in _menu:
        print(str(menu).title() + ", ", end="")

    print()
    while True:
        choisse = input(_str).strip().lower()
        if choisse in _menu:
            return choisse
        else:
            print("Name of menu unknown please retry")


def main():
    menuActions = {
        "add item": AddItem,
        "remove item": RemoveItem,
        "display inventory": DisplayInventory,
        "search item": SearchItem,
        "quit": None,
    }

    inventory = {}

    while True:
        print()
        print("--------------------------------------")
        choice = GetMenu(menuActions, "Chose a menu between : ")

        if choice == "quit":
            break

        if choice in menuActions:
            menuActions[choice](inventory)


main()
