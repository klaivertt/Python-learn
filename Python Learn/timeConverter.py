def GetInt(_str, _min = 0, _max = 0):
    while True:
        try:
            nb = int(input(_str))
            if _min < nb < _max :
                return nb
            else :
                print(f"please enter a number between {_min} and {_max} ")
        except ValueError:
            print("Enter an valid int")
            

def main():
    while True:
        
        choice = GetInt("Chose a conversion between : ")
        print("1. minutes -> seconds")
        print("2. hours -> minutes")
        print("3. days -> hours")  
        print("0. to exit")
        
        match choice:
            case 0:
                break
            case 1:
                nb = GetInt("Enter number of minutes you want to convert")
                print(f"{nb} minutes in secounds = {nb * 60}")
            case 2:
                nb = GetInt("Enter number of hours you want to convert")
                print(f"{nb} hours in minutes = {nb * 60}")
            case 3:
                nb = GetInt("Enter number of hours you want to convert")
                print(f"{nb} hours in minutes = {nb * 24}")
        
main()
            
                