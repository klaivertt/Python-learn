import random

def GetIntBetween(_prompt, _nb1 = 0, _nb2 = 0):
    while True:
        try :
            nb = int(input(_prompt))
            if ((_nb1 <= nb) and (nb <= _nb2)) : 
                return nb
            else :
                print(f"Please enter a number between {_nb1} and {_nb2}")
        except ValueError:
            print("Please enter a valid integer.")
        
def main():
    
    rngNb = random.randint(1,100)
    attempt = 0
    
    while True : 
        nb =  GetIntBetween("Choise a number between 0 and 100 :", 1 , 100)
        attempt +=1
        if (nb == rngNb):
            print(f"Correct! the right number is {rngNb}")
            print(f"You found the number in {attempt} attempts.")
            break
        elif (nb > rngNb):
            print(f"Guess: {nb}")
            print("Too high")
        else :
            print(f"Guess: {nb}")
            print("Too low")

main() 
            
                