def DisplayMultiplicationTable(_nb):
    print()
    print("------------------------------------")
    for i in range(10):
        print(f"{i + 1}: {i+ 1} x {_nb} = {(i+ 1) * _nb}")
    
def GetInt(_str):
    while True:
        try:
            return int(input(_str))
        except ValueError:
            print("Please enter an valid int")

def main():
    
    nb = GetInt("Enter a number to multyplie it : ")
    DisplayMultiplicationTable(nb)

main()