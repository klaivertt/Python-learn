def main():

    isOk = False

    while not isOk :  
        try :
            x = int(input("What's x ? "))
        except ValueError:
            print("x is not an integer")
            isOk = False
        else:
            print(f"x is {x}")
            isOk = True
main()