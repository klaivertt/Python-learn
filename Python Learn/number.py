def get_int():
#Ask to user an integer if the result isn't an integer retry the while
    while True :  
        try :
            x = int(input("What's x ? "))
            return x 
        except ValueError:
            print("x is not an integer")

def main():
    print(f"x is {get_int()}")
            
main()