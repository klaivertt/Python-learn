def IsValidPassword(_password):
        print("you choise :" + _password + " as password")
        if len(_password) < 8 :
            print("password to short")
            return False
        else : 
            print("your password have the required length")
            
            capitalised = False 
            lower = False 
            haveANumber = False
            
            for letter in _password:
                
                if(letter.islower()):
                    lower = True
                if(letter.isupper()):
                    capitalised = True
                if(letter.isdigit()):
                    haveANumber = True
                                
                if capitalised and lower and haveANumber:
                    break
                
                
            if(capitalised and lower and haveANumber) :
                print("your password have one capitalised letter and lower letter and a number")
                return True
            else :
                print("your password miss one capitalised letter or lower letter or a number")
                return False
    
      
def main():
    password = ""
    while True:
        password = input("choise a password : ")
        if IsValidPassword(password):
            break
        
    print("your password is availlable")

main()