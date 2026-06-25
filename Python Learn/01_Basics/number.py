def GetInt(_prompt):
#Ask to user an integer if the result isn't an integer retry the while
    while True :  
        try :
            return int(input(_prompt))
        except ValueError:
            # print("x is not an integer")
            pass

def main():
    print(f"x is {GetInt("What's x ? ")}")
            
main()  