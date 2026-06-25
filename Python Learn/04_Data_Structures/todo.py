def AddTo(_todo):
    print("You wand add a task to your todo ?")
    print("Yes or No")
    
    choice = ""
    while True:
        choice = input("Your choise : ").strip().lower()
        
        if choice == "yes" or choice == "no":
            break
        else:
            print("Please enter 'Yes' or 'No'")
    
    if choice == "no":
        return
    
    name = input("Choise a name for your task : ").strip().lower()
    
    print(f"You choise {name.title()}")
    
    description = input("Choise a Description for your task : ").strip()
    
    _todo[name] = description            
    

def RemoveTo(_todo):
    print("Choose an task to remove :")
    for task in _todo:
        print(str(task).title())
        
    while True:
        choice = input("Choise a Taks you want to remove : ").strip().lower()
        
        if choice in _todo:
            break
        else:
            print("Please enter an valid task")
    
    
    print(f"Do you realy want to delete this task : {choice} ?")
    print("Yes or No")
    while True:
        choice2 = input("Your choise : ").strip().lower()
        
        if choice2 == "yes" or choice2 == "no":
            break
        else:
            print("Please enter 'Yes' or 'No'")
    
    if choice2 == "no":
        return
    else :
        del _todo[choice]        
    
    
    
def Display(_todo):
    for task in _todo:
        print(task, ":", _todo[task])
    
# def Modifie(_todo):
    
    
def GetMenu(_menu, _str):
    print("Navigate into menu choice: ", end="")
    for menu in _menu:
        print(str(menu).title() + ", ", end="")
    
    print()
    while True:
        choice = input(_str).strip().lower()
        if choice in _menu:
            return choice
        else:            
            print("Name of menu unknown please retry")
        
        
    
def main():
    todo = {}
    
    funct = {
        "add": AddTo,
        "remove": RemoveTo,
        "display": Display,
        "quit" : None
    }
    
    while True:
        choice = GetMenu(funct,"Choise a menu between : ")
        
        if choice == "quit":
            break
        
        if choice in funct:
            funct[choice](todo)
            

main()