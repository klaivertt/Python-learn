import secrets
import string

def GetInt(_str, _min = 0):
    while True:
        try:
            nb = int(input(_str))
            
            if nb > _min:
                return nb
            else:
                print(f"Please enter an int greater than {_min}")
        except ValueError:
            print("Please enter an valid int")
                
def YesNo(_str):
    while True:
         choice = input(_str).strip().lower()
         
         if choice == "yes" or choice == "no":
             if choice == "yes":
                 return True
             else:
                 return False
         else :
             print("Please enter 'Yes' or 'No'")
        
                

def main():
    size = GetInt("Choice size of your password : ", 8)
    
    digit = YesNo("Do you want use Digit, 'yes' or 'no' ? ")    
    specialCaracter = YesNo("Do you want use Special Caractere, 'yes' or 'no' ? ")    
    
    password = ""
    allChars = string.ascii_letters
    
    if specialCaracter:
       allChars += string.punctuation
    
    if digit:
        allChars += string.digits
        
    for _ in range(size):
        password += secrets.choice(allChars)
    
    print(f'Final Password :\n{password}')
    
    with open("password.txt", "w") as file:
        file.write(f'Final Password :\n')
        
        nb = 0
        row = ""
        for char in password:
            row += char
            nb += 1
            if nb % 250 == 0:
                file.write(f"{row}\n")
                row = ""
            

if __name__ == "__main__":
    main()

