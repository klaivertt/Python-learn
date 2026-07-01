import random
import os


def GetInt(_str, _min = 0, _max = 10):
    while True:
        try:
            nb = int(input(_str))
            
            if _min < nb < _max:
                return nb
            else:
                print(f"Please enter en int between {_min} and {_max}")
        
        except ValueError:
            print("Please enter an valid int")

def ClearS():
    os.system('cls' if os.name == 'nt' else 'clear')

def PrintTitle(_title):
    print("\n" + "=" * 50)
    print(_title.center(50))
    print("=" * 50 + "\n")
    
def PrintSubTitle(_subTittle):
    print("\n" + "─" * 40)
    print(_subTittle.center(40))
    print("─" * 40)
        
def AskChoice(_str, _action):
    prompt = " | ".join(_action)
    return input(f"\n{_str} :\n {prompt}: ").strip().lower()