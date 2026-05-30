def Choisse()
name = input("choise one opération between, Add, Sub, Mult, Div,Mod")
    while True
      name = input("choise one opération ?")
      match name:
         case "Add" | "Sub" |"Mult"|"Div" |"Mod":
            return name
        case _:
      
def GetInt(_prompt):
   while True :  
        try :
            return int(input(_prompt))
        except ValueError:
            pass

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
    x = GetInt("Choise X")
    y = GetInt("Choise Y")
    
   choisse = Choisse()
   result = 0
   match choisse:
         case "Add":
         result = Add(x,y)
         case "Sub":
          result = Sub(x,y)
         case "Mult":
          result = Mult(x,y)
         case "Div":
          result = Div(x,y)
         case "Mod":
          result = Mod(x,y)
        case _:
   
   print(f"The result of your calcul is {result}")
   
main()