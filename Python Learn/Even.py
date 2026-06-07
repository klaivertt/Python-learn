def IsEven(_n):
    if ((_n%2) == 0):
        return True
    else :
        return False

def GetInt(_prompt):
    while True:
        try:
            return int(input(_prompt))        
        except ValueError:
            pass

def main():
    number = GetInt("Choise a number :")
    
    print(f"{number} is even?, {number} is: ", end="")
    result = ""
    
    if IsEven(number):
        print("Even")
    else:
        print("Odd")
    
    
main()