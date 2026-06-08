def main():
    password = ""
    while True:
        password = input("choise a password : ")
        
        print("you choise :" + password + "as password")
        if len(password) < 8 :
            print("password to short")
        else : 
            print("your password have the required length")
            
            capitalised = False 
            lower = False 
            haveANumber = False
            
            for i in range(len(password)):
                
                if(password[i].islower()):
                    lower = True
                if(password[i].isupper()):
                    capitalised = True
                    lower = True
                if(password[i].isdigit()):
                    haveANumber = True
                                
                if capitalised and lower and haveANumber:
                    break
                
                
            if(capitalised and lower and haveANumber) :
                print("your password have one capitalised letter and lower letter and a number")
                break
            else :
                 print("your password miss one capitalised letter or lower letter or a number")
    print("your password is availlable")

main()