def GetInt(_prompt):
    while True :
        try :
            return int(input(_prompt))
        except ValueError:
            pass




def main() : 
    numb = GetInt("Choise an number : ")
    
    result = ""
    if (numb % 3 == 0):
        result += "Fizz"
        
    if (numb%5 == 0):
        result += "Buzz"
        
    print(result)  

main()