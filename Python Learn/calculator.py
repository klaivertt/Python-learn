def Choisse()
name = input("choise one opération between, Add, Sub, Mult, Div,Mod")
    while True
      name = input("choise one opération ?")
      match name:
         case "Add" | "Sub" |"Mult"|"Div" |"Mod":
            return name
        case _:

def Add(_a,_b):
   return _a + _b

def Sub(_a,_b):
   return _a - _b

def Mult(_a,_b):
   return _a * _b

def Div(_a,_b):
   return _a / _b

def Mod(_a,_b):
   return _a % _b

def main():
    
    
main()